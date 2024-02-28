from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import serializer, models


@api_view(['GET', 'POST'])
def product_list_view(request):
    if request.method == 'GET':
        product = models.Product.objects.all()
        data = serializer.ProductSerializer(product, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializers = serializer.ProductCreateUpdateSerializer(data=request.data)
        if not serializers.is_valid():
            return Response(data={'errors': serializers.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        print(request.data)
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category_id = request.data.get('category_id')

        product = models.Product.objects.create(title=title, description=description, price=price,
                                                category_id=category_id)
        for i in request.data.get("reviews", []):
            models.Review.objects.create(stars=i['stars'], text=i['text'], product=product)


        #product = models.Product.objects.create(**request.data)

        return Response(data=serializer.ProductSerializer(product).data,
                        status=status.HTTP_201_CREATED)
        # return Response(data={'message': 'Данные отправлены'})


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_view(request, id):
    try:
        product = models.Product.objects.get(id=id)
    except models.Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Product not found'})

    if request.method == 'GET':
        data = serializer.ProductSerializer(product).data
        return Response(data=data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={'message': 'Product has been deleted'})
    elif request.method == 'PUT':
        product.title = request.data.get('title')
        product.description = request.data.get('description')
        product.price = request.data.get('price')
        product.category_id = request.data.get('category_id')
        product.save()
        return Response(data=serializer.ProductSerializer(product).data)












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
