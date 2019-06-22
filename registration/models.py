from django.db import models

# Create your models here.


class Business(models.Model):

    TYPE_CHOICES = (('p', 'Private'), ('n', 'NGO'), ('g', 'Government'))
    name = models.CharField(max_length=100)
    b_type = models.CharField(choices=TYPE_CHOICES, max_length=1)
    address = models.CharField(max_length=100)
    services = models.ManyToManyField('Service')

    def __str__(self):
        return self.name        

class Service(models.Model):

    service = models.CharField(max_length=100)

    def __str__(self):
        return self.service