from rest_framework import serializers
from users.models import *

# Serializers define the API representation.
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['pk', 'username', 'email', 'is_staff']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            'pk', 'name',
        ]

# class EndcitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = City
#         fields = [
#             'name',
#         ]
#
# class NeedListSerializer(serializers.ModelSerializer):
#     start_city = StartcitySerializer()
#     end_city = EndcitySerializer()
#     class Meta:
#         model = Need
#         fields = [
#             'image',
#             'start_city',
#             'end_city',
#             'start_date',
#             'end_date',
#             'good_name',
#             'offer_price',
#             'message',
#         ]
#
# class ServiceListSerializer(serializers.ModelSerializer):
#     start_city = StartcitySerializer()
#     end_city = EndcitySerializer()
#     class Meta:
#         model = Service
#         fields = [
#             'image',
#             'start_city',
#             'end_city',
#             'start_date',
#             'end_date',
#             'ask_price',
#             'message',
#         ]