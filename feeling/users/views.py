from django.shortcuts import render
from django.contrib.auth import logout
def dashboard(request):
    return render(request,'users/dashboard.html')
