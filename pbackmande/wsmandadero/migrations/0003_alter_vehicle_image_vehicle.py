# Generated by Django 5.0.2 on 2024-02-28 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wsmandadero', '0002_account_mander_request_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='image_vehicle',
            field=models.ImageField(max_length=255, null=True, upload_to='imgVehicles'),
        ),
    ]
