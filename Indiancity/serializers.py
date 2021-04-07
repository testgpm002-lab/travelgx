from rest_framework import serializers
from . models import CityList

class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityList
        fields = '__all__'
