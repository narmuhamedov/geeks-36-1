from rest_framework import serializers
from . import models


# 1способ прописка отдельного сериализатора
# 2способ вывода прописка своего метода.

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = 'id name'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    category = serializers.SerializerMethodField()
    #reviews = ReviewSerializer(many=True)

    reviews = serializers.SerializerMethodField()

    class Meta:
        model = models.Product
        fields = "id title price category reviews count_reviews all_reviews".split()
        # fields = "__all__"

    def get_category(self, product):
        try:
            return product.category.name
        except:
            return "No Category"

    def get_reviews(self, product):
        #serializer = ReviewSerializer(product.reviews.all(), many=True)
        serializer = ReviewSerializer(models.Review.objects.filter(author__isnull=False,
                                                                   product=product), many=True)
        return serializer.data
