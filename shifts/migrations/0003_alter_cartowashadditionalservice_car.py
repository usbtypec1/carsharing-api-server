# Generated by Django 5.1.1 on 2024-12-17 03:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0002_alter_shift_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartowashadditionalservice',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additional_services', to='shifts.cartowash'),
        ),
    ]
