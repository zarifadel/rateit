from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# home page view

def home(request):
    
    user_data = 'User is: ' + request.GET['user']

    return render(request, 'index.html', context={'user_data': user_data, 'iterations':list(range(3))})