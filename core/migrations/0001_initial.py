# Generated by Django 4.1.2 on 2022-11-21 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('userid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=40)),
                ('phone_no', models.CharField(max_length=13)),
                ('img', models.ImageField(default='x-avatar.png', upload_to='profiles/')),
                ('gender', models.CharField(default='Male', max_length=8)),
                ('profession', models.CharField(blank=True, max_length=16, null=True)),
                ('place', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('nationality', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userproffile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='room',
            fields=[
                ('room_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('room_no', models.CharField(max_length=10)),
                ('floor', models.CharField(max_length=8)),
                ('gender_preference', models.CharField(default='Male & Female', max_length=15)),
                ('description', models.TextField(blank=True, null=True)),
                ('room_type', models.CharField(max_length=10)),
                ('no_of_beds', models.IntegerField(default=1)),
                ('max_occupants', models.IntegerField(default=1)),
                ('current_occupants', models.IntegerField(default=0)),
                ('room_rent', models.FloatField(blank=True, null=True)),
                ('rent_type', models.CharField(blank=True, max_length=16, null=True)),
                ('appartment_name', models.CharField(max_length=100)),
                ('appartment_address', models.CharField(max_length=250)),
                ('manager', models.TextField(blank=True, null=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_added_by', to='core.profile')),
            ],
        ),
        migrations.CreateModel(
            name='room_review',
            fields=[
                ('comment_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('star', models.FloatField(default=0)),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter_profile', to='core.profile')),
            ],
        ),
        migrations.CreateModel(
            name='room_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='rooms/')),
                ('catagory', models.CharField(max_length=16)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_photo', to='core.room')),
            ],
        ),
    ]