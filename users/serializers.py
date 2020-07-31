from rest_framework import serializers
from users.models import UserProfile

class UsersSerializers(serializers.ModelSerializer):
  class Meta:
        model = UserProfile
        fields = '__all__'
