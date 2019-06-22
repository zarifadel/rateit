from django.shortcuts import render
from django.http import HttpResponse
from registration.models import Business

# Create your views here.

# home page view

def home(request):

    businesses = Business.objects.all()

    return render(request, 'index.html', context={'businesses': businesses})