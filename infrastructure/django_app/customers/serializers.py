from rest_framework import serializers

class CustomerInputSerializer(serializers.Serializer):
    cpf = serializers.CharField(allow_null=True, required=False)
    name = serializers.CharField(allow_null=True, required=False)
    email = serializers.EmailField(allow_null=True, required=False)

class CustomerOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    cpf = serializers.CharField(allow_null=True)
    name = serializers.CharField(allow_null=True)
    email = serializers.EmailField(allow_null=True)
