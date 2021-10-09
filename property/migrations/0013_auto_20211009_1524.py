# Generated by Django 3.1.7 on 2021-10-09 12:24

import phonenumbers

from django.db import migrations


def normalize_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        owners_phonenumber = flat.owners_phonenumber
        owner_pure_phone = phonenumbers.parse(owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(owner_pure_phone):
            flat.owner_pure_phone = owner_pure_phone
            flat.save()
        else:
            continue


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20211009_1436'),
    ]

    operations = [
        migrations.RunPython(normalize_phonenumbers)
    ]