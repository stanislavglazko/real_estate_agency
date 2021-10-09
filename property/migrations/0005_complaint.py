# Generated by Django 3.1.7 on 2021-10-09 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0004_auto_20211009_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст жалобы')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.flat', verbose_name='Квартира, на которую пожаловались')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался')),
            ],
        ),
    ]
