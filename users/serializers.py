from rest_framework import serializers
from users.models import *

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            'pk', 'name',
        ]