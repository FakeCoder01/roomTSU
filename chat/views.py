from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *

from django.http import JsonResponse
from django.db.models import Q
import json
# Create your views here.

@login_required(login_url='/login')
def charView(request):
    context = {
        'message_group' : ChatRoom.objects.filter(Q(user1=request.user.userprofile) | Q(user2=request.user.userprofile)),
        'user' : request.user.userprofile,
    }

    return render(request, 'chat/chat.html', context)

@login_required(login_url='/login')
def getMessages(request):
    if request.method == 'GET':
        chat_room_id = request.GET['chat_room_id']

        if ChatRoom.objects.filter(Q(access_key=chat_room_id) & (Q(user1=request.user.userprofile) | Q(user2=request.user.userprofile))).exists():
            c_room = ChatRoom.objects.get(Q(access_key=chat_room_id) & (Q(user1=request.user.userprofile) | Q(user2=request.user.userprofile)))
            response = c_room.get_room_messages()
            return JsonResponse(json.dumps({
                'status_code' : 200,
                'msg' : 'success',
                'data' : response,
                'chat_room': c_room.access_key,
            }), safe=False)
        return JsonResponse({'msg' : 'failed (1)'}, safe=False)    
    return JsonResponse({'msg' : 'failed'}, safe=False)



@login_required(login_url='/login')
def addMessages(request):
    if request.method == 'POST':
        text = request.POST['message']
        chat_room_id = request.POST['chat_room_id']

        if ChatRoom.objects.filter(Q(access_key=chat_room_id) & (Q(user1=request.user.userprofile) | Q(user2=request.user.userprofile))).exists():
            c_room = ChatRoom.objects.get(Q(access_key=chat_room_id) & (Q(user1=request.user.userprofile) | Q(user2=request.user.userprofile)))
            
            addNewMessage = chat_message.objects.create(
                text = text,
                chat_room = c_room,
                sender = request.user.userprofile,
                receiver = c_room.user1 if c_room.user2 == request.user.userprofile else c_room.user2  
            )
            return JsonResponse(json.dumps({
                'status_code' : 200,
                'msg' : 'sent',
            }), safe=False)
        return JsonResponse({'msg' : 'failed (1)'}, safe=False)  
    return JsonResponse(json.dumps({'msg' : 'failed'}), safe=False)



@login_required(login_url='/login')
def createChatRoom(request):
    if request.method == 'POST':
        userid = request.POST['userid']  
        if not profile.objects.filter(userid=userid).exists():
            return redirect('/?msg=No%20User')
        S_user = profile.objects.get(userid=userid)
        if ChatRoom.objects.filter(user1=request.user.userprofile, user2=S_user).exists() or ChatRoom.objects.filter(user2=request.user.userprofile, user1=S_user).exists():
            return redirect(f"/chat/#")
        newChatRoom = ChatRoom.objects.create(
            user1 = request.user.userprofile,
            user2 = S_user
        )
        return redirect(f"/chat/#{newChatRoom.access_key}")  
    return JsonResponse(json.dumps({'msg' : 'failed'}), safe=False)



