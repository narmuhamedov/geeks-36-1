from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import serializer, models


@api_view(['GET'])
def product_list_view(request):
    product = models.Product.objects.all()
    data = serializer.ProductSerializer(product, many=True).data
    return Response(data=data)


@api_view(['GET'])
def product_detail_view(request, id):
    try:
        product_id = models.Product.objects.get(id=id)
    except models.Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Product not found'})
    data = serializer.ProductSerializer(product_id).data
    return Response(data=data)


@api_view(['GET'])
def test(request):
    context = {
        'integer': 100,
        'string': 'hello world',
        'boolean': True,
        'list': [
            1, 2, 3
        ]
    }
    return Response(data=context)
