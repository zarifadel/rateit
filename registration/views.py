from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Service, Business
import json
# Create your views here.


# HttpRequest
def register(request):
    print('http method: ',request.method)

    services = Service.objects.all()

    if request.method == 'GET':
        return render(request, 'registration.html', context={'services': services, 'editing':False})
    else:

        name = request.POST.get('name')
        b_type = request.POST.get('_type')
        address = request.POST.get('address')
        services = request.POST.getlist('services')

        business = Business(name=name, b_type=b_type, address=address)
        business.save()

        for service in services:
            business.services.add(int(service))

        return HttpResponseRedirect('/')

def update(request):

    if request.method == 'GET':
        id = request.GET.get('id')

        business = Business.objects.get(id=int(id))

        types = business.TYPE_CHOICES

        services = Service.objects.all()

        context = {
            'business': business,
            'editing': True,
            'types': types,
            'services': services,
            'business_services': business.services.all().values_list('id', flat=True)
        }

        return render(request, 'registration.html', context=context)
    elif request.method == 'POST':
        

        services = request.POST.getlist('services')
        all_fileds = request.POST.dict()
        del all_fileds['services']
        del all_fileds['csrfmiddlewaretoken']

        
        print(all_fileds)
        business, created = Business.objects.update_or_create(id=request.POST.get('id'), defaults=all_fileds)

        for service in services:
            if not business.services.all().filter(id=service).exists():
                business.services.add(service)

        






        
