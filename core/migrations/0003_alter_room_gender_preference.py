# Generated by Django 4.1.2 on 2022-11-23 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_profile_user_alter_room_image_catagory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='gender_preference',
            field=models.CharField(default='Male/Female', max_length=15),
        ),
    ]
