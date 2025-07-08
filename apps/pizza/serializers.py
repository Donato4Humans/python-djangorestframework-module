from rest_framework import serializers

from apps.pizza.models import PizzaModel


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaModel
        fields = ('id', 'name', 'size', 'price', 'created_at', 'updated_at')
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=50)
    # size = serializers.IntegerField()
    # price = serializers.FloatField()
    # created_at = serializers.DateTimeField(read_only=True)
    # updated_at = serializers.DateTimeField(read_only=True)
    #
    # def create(self, validated_data:dict):
    #     return PizzaModel.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data:dict):
    #     for key, value in validated_data.items():
    #         setattr(instance, key, value)
    #     instance.save()
    #     return instance