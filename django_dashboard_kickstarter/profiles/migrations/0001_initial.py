# Generated by Django 5.1.1 on 2024-09-26 10:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=240)),
                ('last_name', models.CharField(blank=True, max_length=240)),
                ('company_name', models.CharField(blank=True, max_length=240)),
                ('city', models.TextField(blank=True, max_length=1500)),
                ('address', models.CharField(blank=True, max_length=240)),
                ('postal_code', models.CharField(max_length=50, null=True)),
                ('province', models.CharField(max_length=200, null=True)),
                ('region', models.CharField(max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=240)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('other_data', models.TextField(blank=True)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('profile_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile_type')),
            ],
        ),
    ]
