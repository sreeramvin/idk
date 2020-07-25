from rest_framework import viewsets, permissions
from users.models import Users
from users.serializers import UsersSerializers

class UsersViewSet(viewsets.ModelViewSet):
    queryset =Users.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UsersSerializers
