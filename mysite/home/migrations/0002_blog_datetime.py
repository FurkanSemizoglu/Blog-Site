# Generated by Django 4.2.3 on 2023-08-25 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='datetime',
            field=models.DateTimeField(auto_now=True, verbose_name='tarih'),
        ),
    ]