# Generated by Django 4.2 on 2023-04-15 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=10)),
                ('postal_code', models.IntegerField()),
                ('contract_start_date', models.DateField(blank=True, null=True)),
                ('contract_end_date', models.DateField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('device_id', models.CharField(max_length=255)),
                ('ip_address', models.CharField(blank=True, max_length=15, null=True)),
                ('mac_address', models.CharField(blank=True, max_length=17, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=20)),
                ('wait_bags', models.IntegerField(blank=True, default=3)),
                ('initial_hold', models.IntegerField(default=600)),
                ('circle', models.IntegerField(default=21)),
                ('feed_time', models.IntegerField(default=6)),
                ('circle_hold', models.IntegerField(default=15)),
                ('galla_clear_time', models.IntegerField(default=20)),
                ('actual_hold', models.IntegerField(default=900)),
                ('overload_hold', models.IntegerField(default=2100)),
                ('galla_vibrator_status', models.BooleanField(default=True)),
                ('hopper_vibrator_status', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devicedata.company')),
            ],
        ),
        migrations.CreateModel(
            name='Milldata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('katta_time', models.DateTimeField()),
                ('katta_weight', models.FloatField(blank=True, null=True)),
                ('initial_hold', models.IntegerField()),
                ('circle', models.IntegerField()),
                ('feed_time', models.IntegerField()),
                ('circle_hold', models.IntegerField()),
                ('galla_clear_time', models.IntegerField()),
                ('actual_hold', models.IntegerField()),
                ('overload_hold', models.IntegerField()),
                ('feed_status', models.BooleanField(default=True)),
                ('overload_status', models.BooleanField(default=False)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devicedata.device')),
            ],
        ),
    ]
