from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class profile(models.Model):
    userid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userprofile")
    full_name = models.CharField(max_length=40)
    phone_no = models.CharField(max_length=13)
    img = models.ImageField(upload_to='profiles/', default="x-avatar.png")
    gender = models.CharField(max_length=8, default="Male")
    profession = models.CharField(max_length=16, null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)

    address = models.CharField(max_length=100, null=True, blank=True)
    nationality = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.full_name



class room(models.Model):
    room_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    added_by = models.ForeignKey(profile, on_delete=models.CASCADE, related_name="room_added_by")
    room_no = models.CharField(max_length=10)
    floor = models.CharField(max_length=8)
    gender_preference = models.CharField(max_length=15, default="Male/Female")
    description = models.TextField(null=True, blank=True)
    room_type = models.CharField(max_length=10)
    no_of_beds = models.IntegerField(default=1)
    max_occupants = models.IntegerField(default=1)
    current_occupants = models.IntegerField(default=0)

    room_rent = models.FloatField(null=True, blank=True)
    rent_type = models.CharField(max_length=16, null=True, blank=True)


    appartment_name = models.CharField(max_length=100)
    appartment_address = models.CharField(max_length=250)
    manager = models.TextField(null=True, blank=True)


    def __str__(self) -> str:
        return str(self.room_id)


class room_review(models.Model):
    comment_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    commenter = models.ForeignKey(profile, on_delete=models.CASCADE, related_name="commenter_profile")
    text = models.TextField()
    star = models.FloatField(default=0)

    def __str__(self) -> str:
        return self.comment_id



class room_image(models.Model):
    room = models.ForeignKey(room, on_delete=models.CASCADE, related_name="room_photo")
    img = models.ImageField(upload_to='rooms/', null=True, blank=True)
    catagory = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self) -> str:
        return self.room