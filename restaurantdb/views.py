
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

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
