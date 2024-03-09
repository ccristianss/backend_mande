# Generated by Django 5.0.2 on 2024-03-02 01:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wsmandadero', '0002_account_mander_request_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_id_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wsmandadero.account', unique=True),
        ),
    ]
