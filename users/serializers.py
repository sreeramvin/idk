from rest_framework import serializers
from users.models import Users

class UsersSerializers(serializers.ModelSerializer):
  class Meta:
        model = Users
        fields = ['id', 'name', 'phone_number', 'address', 'temperature', 'oxygen_saturation']

