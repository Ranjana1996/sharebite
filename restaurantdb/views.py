from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item, Section, Modifier
from .serializer import ItemSerializer, SectionSerializer, ModifierSerializer, UserSerializer
from django.contrib.auth.models import User


# Create your views here.

class ModifierViewSet(viewsets.ModelViewSet):
    queryset = Modifier.objects.all()
    serializer_class = ModifierSerializer

    def get_queryset(self):
        modifiers = Modifier.objects.all()
        return modifiers


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        items = Item.objects.all()
        return items

    def create(self, request, *args, **kwargs):
        data = request.data
        new_item = Item.objects.create(section=Section.objects.get(id=data["section"]), name=data['name'],
                                       description=data['description'], price=data['price'])
        new_item.save()
        for modifier in data['modifiers']:
            modifier_object = Modifier.objects.get(id=modifier['id'])
            new_item.modifiers.add(modifier_object)
        serializer = ItemSerializer(new_item)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        item_object = self.get_object()
        data = request.data
        section = Section.objects.get(id=data["section"])
        item_object.section =section
        item_object.name=data['name']
        item_object.description=data['description']
        item_object.price=data['price']
        item_object.save()
        item_object.modifiers.clear()
        for modifier in data['modifiers']:
            modifier_object = Modifier.objects.get(id=modifier['id'])
            item_object.modifiers.add(modifier_object)
        serializer = ItemSerializer(item_object)

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        item_object = self.get_object()
        data = request.data
        try:
            section = Section.objects.get(id=data["section"])
            item_object.section = section
        except KeyError:
            pass
        item_object.name = data.get('name',item_object.name)
        item_object.description = data.get('description',item_object.description)
        item_object.price = data.get('price',item_object.price)
        item_object.save()
        modifiers = data.get('modifiers',item_object.modifiers)
        item_object.modifiers.clear()
        for modifier in modifiers:
            modifier_object = Modifier.objects.get(id=modifier['id'])
            item_object.modifiers.add(modifier_object)
        serializer = ItemSerializer(item_object)

        return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        item.delete()
        response_message = {"message": "Item has been deleted"}
        return Response(response_message)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
