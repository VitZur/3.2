from rest_framework import serializers
from .models import Products, Stock, StockProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity','price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']  # Добавляем поле 'address'

    def create(self, validated_data):

        positions = validated_data.pop('positions')


        stock = Stock.objects.create(**validated_data)


        for position in positions:
            StockProduct.objects.create(stock=stock, **position)

        return stock

    def update(self, instance, validated_data):

        positions = validated_data.pop('positions')


        instance.address = validated_data.get('address', instance.address)
        instance.save()


        instance.positions.all().delete()
        for position in positions:
            StockProduct.objects.create(stock=instance, **position)

        return instance
