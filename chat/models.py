from django.db import models
from django.utils.crypto import get_random_string
from core.models import *
# Create your models here.



class ChatRoom(models.Model):
    user1 = models.ForeignKey(profile, related_name="chat_user1", on_delete=models.CASCADE)
    user2 = models.ForeignKey(profile, related_name="chat_user2", on_delete=models.CASCADE)
    access_key = models.CharField(max_length=16, default=get_random_string(16), unique=True)
    def get_room_messages(self):
        messages = list(chat_message.objects.filter(chat_room=self))
        data = []

        for m in messages:
            data.append({
                'message' : m.text,
                'sender' : m.sender,
                'receiver' : m.receiver,
                'sent_at' : str(m.created_at)
            })
        return data
    def __str__(self):
        return self.access_key

class chat_message(models.Model):
    text = models.TextField(null=True, blank=True)
    chat_room = models.ForeignKey(ChatRoom, related_name="chatroom", on_delete=models.CASCADE)
    sender = models.ForeignKey(profile, related_name="chat_sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(profile, related_name="chat_receiver", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.sender + ' ' + str(self.created_at)  + ' (' + self.sender_type + ')' 