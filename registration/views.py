from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# HttpRequest
def register(request):
    return render(request, 'registration.html')