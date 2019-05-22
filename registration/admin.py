from django.contrib import admin
from .models import Business, Service

# Register your models here.

class BusinessAdmin(admin.ModelAdmin):
    pass

admin.site.register(Business, BusinessAdmin)

class ServiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Service, ServiceAdmin)