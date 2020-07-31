from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view
from users.models import Users
from users.serializers import UsersSerializers
from rest_framework import viewsets, permissions

# Create your views here.

class UserList(viewsets.ModelViewSet):
    def get(self,request):
        user=Users.objects.all()
        serializer=UsersSerializers(user,many=True)
        return Response(serializer.data)
   
    def post(self, request):
        serializer=UsersSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(users.data, status=status.HTTP_201_CREATED)
        else:
            return Response(users.errors, status=status.HTTP_400_BAD_REQUEST)