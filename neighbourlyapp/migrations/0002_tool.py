# Generated by Django 2.2.4 on 2021-03-04 03:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourlyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=60)),
                ('start_date', models.DateTimeField(default=datetime.date.today)),
                ('end_date', models.DateTimeField(default=datetime.date.today)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tools', to='neighbourlyapp.User')),
            ],
        ),
    ]
