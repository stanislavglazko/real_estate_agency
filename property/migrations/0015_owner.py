# Generated by Django 3.1.7 on 2021-10-09 12:56

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20211009_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('phonenumber', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('owner_pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, null=True, region=None, verbose_name='Нормализированный номер владельца')),
                ('flats', models.ManyToManyField(related_name='owner_flats', to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]
