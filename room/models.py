from django.db import models
from core.models import *
import uuid
# Create your models here.


class RoomReq(models.Model):
    r_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    room = models.ForeignKey(room, related_name="room_req", on_delete=models.CASCADE)
    owner = models.ForeignKey(profile, related_name="owner_req", on_delete=models.CASCADE)
    user = models.ForeignKey(profile, related_name="user_req", on_delete=models.CASCADE)