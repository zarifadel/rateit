# Generated by Django 2.1.1 on 2019-05-22 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20190522_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='services',
            field=models.ManyToManyField(to='registration.Service'),
        ),
    ]
