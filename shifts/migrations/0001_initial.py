# Generated by Django 5.1.1 on 2024-10-29 08:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car_washes', '0001_initial'),
        ('staff', '0003_staff_shift_schedule_month_staff_shift_schedule_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarToWash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(choices=[('comfort', 'Comfort'), ('business', 'Business'), ('van', 'Van')], max_length=20)),
                ('car_class', models.CharField(choices=[('comfort', 'Comfort'), ('business', 'Business'), ('van', 'Van')], max_length=16)),
                ('wash_type', models.CharField(choices=[('planned', 'Planned'), ('urgent', 'Urgent')], max_length=16)),
                ('windshield_washer_refilled_bottle_percentage', models.PositiveSmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('car_wash', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='car_washes.carwash')),
            ],
        ),
        migrations.CreateModel(
            name='CarToWashAdditionalService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('count', models.PositiveSmallIntegerField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shifts.cartowash')),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('is_confirmed', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('car_wash', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='car_washes.carwash')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.staff')),
            ],
        ),
        migrations.AddField(
            model_name='cartowash',
            name='shift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shifts.shift'),
        ),
    ]