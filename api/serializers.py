from rest_framework import serializers
from .models import *
class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['address', 'email', 'telephone']

class SupplierSerializer(serializers.ModelSerializer):
    contact_info = ContactInfoSerializer()

    class Meta:
        model = Supplier
        fields = ['id', 'name', 'contact_info', 'items']
        read_only_fields = ['items']

    def create(self, validated_data):
        contact_info_data = validated_data.pop('contact_info')
        contact_info = ContactInfo.objects.create(**contact_info_data)
        supplier = Supplier.objects.create(contact_info=contact_info, **validated_data)
        return supplier

    def update(self, instance, validated_data):
        contact_info_data = validated_data.pop('contact_info')
        contact_info = instance.contact_info

        instance.name = validated_data.get('name', instance.name)
        instance.save()

        contact_info.address = contact_info_data.get('address', contact_info.address)
        contact_info.email = contact_info_data.get('email', contact_info.email)
        contact_info.telephone = contact_info_data.get('telephone', contact_info.telephone)
        contact_info.save()

        return instance

class ItemSerializer(serializers.ModelSerializer):
    suppliers = SupplierSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ['id','name','description', 'price', 'date', 'suppliers']

class ItemCreateSerializer(serializers.ModelSerializer):
    suppliers = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all(), many=True)

    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'date', 'suppliers']

    def create(self, validated_data):
        suppliers_data = validated_data.pop('suppliers')
        item = Item.objects.create(**validated_data)
        item.suppliers.set(suppliers_data)
        return item
    def update(self, instance, validated_data):
        suppliers_data = validated_data.pop('suppliers', None)

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.date = validated_data.get('date', instance.date)
        instance.save()

        if suppliers_data is not None:
            instance.suppliers.set(suppliers_data)

        return instance