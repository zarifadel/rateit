from django.shortcuts import render
from django.http import HttpResponse
from .models import Service, Business
import json
# Create your views here.


# HttpRequest
def register(request):
    print('http method: ',request.method)

    print('data', request.POST)

    
    services = Service.objects.all()



    if request.method == 'GET':
        return render(request, 'registration.html', context={'services': services})
    else:

        params = json.loads(request.POST)
        print(params)
        name = params['name']
        _type = params['_type']
        address = params['address']
        services = params['services']

        print(services)
        print(type(services))

        business = Business(name=name, _type=_type, address=address)
        business.save()

        for service in services:
            business.services.add(int(service))