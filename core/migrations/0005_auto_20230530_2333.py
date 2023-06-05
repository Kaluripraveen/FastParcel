# Generated by Django 3.2.12 on 2023-05-30 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20230530_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='delivery_address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='job',
            name='delivery_lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='delivery_lng',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='delivery_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='job',
            name='delivery_phone',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]