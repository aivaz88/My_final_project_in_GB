# Generated by Django 5.0.2 on 2024-02-12 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_market_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='status_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web_market_app.userstatus'),
        ),
    ]
