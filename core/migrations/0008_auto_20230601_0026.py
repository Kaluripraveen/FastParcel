# Generated by Django 3.2.12 on 2023-06-01 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='delivered_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='delivery_photo',
            field=models.ImageField(blank=True, null=True, upload_to='jobs/delivery_photos/'),
        ),
        migrations.AddField(
            model_name='job',
            name='pickeup_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='pickup_photo',
            field=models.ImageField(blank=True, null=True, upload_to='jobs/pickup_photos/'),
        ),
    ]
