from rest_framework import viewsets, permissions
from users.models import Users
from users.serializers import UsersSerializers

class UsersViewSet(viewsets.ModelViewSet):
    queryset =Users.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UsersSerializers
    def post(self, request):
        serializer=UsersSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(users.data, status=status.HTTP_201_CREATED)
        else:
            return Response(users.errors, status=status.HTTP_400_BAD_REQUEST)
