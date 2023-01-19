from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Section,Item,Modifier
from drf_writable_nested import WritableNestedModelSerializer



# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')



class ModifierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Modifier
        fields = ("id", "description")

class ItemSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    #modifiers = serializers.SlugRelatedField(many=True, queryset=Modifier.objects.all(),slug_field="description")
    #modifiers = ModifierSerializer(many=True)
    #section = SectionSerializer(read_only=True)
    class Meta:
        ordering = ['name']
        model = Item
        fields = ("id", "name", "description", "price", "modifiers","section")
        extra_kwargs = {'modifiers': {'required': False}}
        depth = 1

    # def create(self, validated_data):
    #     modifier_data = validated_data.pop('modifiers')
    #     item_data = Item.objects.create(**validated_data)
    #     for modifier in modifier_data:
    #         obj= Modifier.get_or_create(**modifier)
    #         item_data.modifiers.add(obj)
    #         item_data.save()


class SectionSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = fields = ("id", "name", "description", 'items')






