# Generated by Django 2.1.1 on 2019-06-22 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_business_services'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='_type',
            new_name='b_type',
        ),
    ]
