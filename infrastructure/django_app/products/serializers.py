from rest_framework import serializers

class CategoryInputSerializer(serializers.Serializer):
    name = serializers.CharField()

class CategoryOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

class ProductInputSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    category = CategoryInputSerializer()
    image = serializers.ImageField(required=False, allow_null=True)

class ProductOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    category = CategoryOutputSerializer()
    image_url = serializers.URLField(allow_null=True, required=False)
