# Generated by Django 3.1.7 on 2021-10-10 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_auto_20211010_0908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]
