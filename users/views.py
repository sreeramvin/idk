from django.shortcuts import render
from .models import UserProfile

def Table(request):
    users=UserProfile.objects.all()
    return render(request,'users/table.html',{'users':users})