# Generated by Django 5.0.2 on 2024-03-02 01:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wsmandadero', '0003_alter_user_account_id_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mander',
            name='user_id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wsmandadero.user', unique=True),
        ),
    ]