# Generated by Django 5.0.2 on 2024-02-08 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0004_alter_vehicle_brand_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='brand_vehicle',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model_vehicle',
            field=models.DateField(max_length=4),
        ),
    ]