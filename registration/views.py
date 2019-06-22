from django.shortcuts import render
from django.http import HttpResponse
from .models import Service, Business
import json
# Create your views here.


# HttpRequest
def register(request):
    print('http method: ',request.method)

    services = Service.objects.all()

    if request.method == 'GET':
        return render(request, 'registration.html', context={'services': services})
    else:

        name = request.POST.get('name')
        b_type = request.POST.get('_type')
        address = request.POST.get('address')
        services = request.POST.getlist('services')

        business = Business(name=name, b_type=b_type, address=address)
        business.save()

        for service in services:
            business.services.add(int(service))