from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework import permissions
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from users.models import Users
from users.serializers import UsersSerializers
from rest_framework import viewsets, permissions

# Create your views here.

class UserList(APIView):
    permission_classes = [
        permissions.AllowAny
    ]
    
    def get(self, request, format=None):
        user = Users.objects.all()
        users = UsersSerializers(user, many=True)
        return Response(users.data)

    def post(self, request, format=None):
        users = UsersSerializers(data=request.data)
        if users.is_valid():
            users.save()
            return Response(users.data, status=status.HTTP_201_CREATED)
        return Response(users.errors, status=status.HTTP_400_BAD_REQUEST)
class UserDetail(APIView):

    permission_classes = [
        permissions.AllowAny
    ]
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        users = UsersSerializers(user)
        return Response(users.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        users = UsersSerializers(user, data=request.data)
        if users.is_valid():
            users.save()
            return Response(users.data)
        return Response(users.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)