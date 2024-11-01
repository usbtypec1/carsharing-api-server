# Generated by Django 5.1.1 on 2024-11-01 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_remove_staff_shift_schedule_month_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': 'staff', 'verbose_name_plural': 'staff'},
        ),
        migrations.AlterModelOptions(
            name='staffavailabledate',
            options={'verbose_name': 'staff available date', 'verbose_name_plural': 'staff available dates'},
        ),
        migrations.AlterUniqueTogether(
            name='staffavailabledate',
            unique_together={('staff', 'month', 'year')},
        ),
    ]
