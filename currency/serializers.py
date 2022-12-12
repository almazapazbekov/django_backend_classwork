from rest_framework import serializers

from .models import CurrencyName, CurrencyRate, Student


class CurrencyNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyName
        fields = '__all__'


class CurrencyRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRate
        fields = '__all__'


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    birth_date = serializers.DateField()
    email = serializers.EmailField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.email = validated_data['email']
        instance.birth_date = validated_data['birth_date']
        instance.save()
        return instance



