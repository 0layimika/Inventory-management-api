from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Item, Supplier
from .serializers import SupplierSerializer,ItemSerializer, ItemCreateSerializer
from rest_framework import status
from rest_framework.generics import get_object_or_404

#Get all suppliers and create a new supplier
@api_view(['GET', 'POST'])
def suppliers(request):
    if request.method == 'GET':
        suppliers = Supplier.objects.all()
        serialized = SupplierSerializer(suppliers, many=True)
        return Response(serialized.data)
    elif request.method == 'POST':
        serialized=SupplierSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

#Get specific supplier, edit supplier detail and delete supplier
@api_view(['GET','PUT','DELETE'])
def supplier(request,id):
    supplier = get_object_or_404(Supplier,pk=id)
    if request.method == 'GET':
        serialized = SupplierSerializer(supplier)
        return Response(serialized.data)
    if request.method == 'PUT':
        serialized = SupplierSerializer(supplier,data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        supplier.delete()
        return Response("Supplier Deleted",status=status.HTTP_204_NO_CONTENT)

#Get all items and add a new item
@api_view(['GET', 'POST'])
def items(request):
    if request.method == 'GET':
        items = Item.objects.all();
        serialized = ItemSerializer(items, many=True)
        return Response(serialized.data)
    if request.method == 'POST':
        serialized = ItemCreateSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

#Get specific item, update item, delete time
@api_view(['GET','PUT','DELETE'])
def item(request, id):
    items = get_object_or_404(Item,pk=id)
    if request.method == 'GET':
        serialized = ItemSerializer(items)
        return Response(serialized.data)
    if request.method == 'PUT':
        serialized = ItemCreateSerializer(items, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        items.delete()
        return Response("Item Deleted", status=status.HTTP_204_NO_CONTENT)


