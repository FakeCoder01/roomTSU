from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
import json
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from uuid import UUID
from core.models import *
from .forms import AddRoomForm

# Create your views here.


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj) :
        try:
            if isinstance(obj, UUID):
                return obj.hex
            return json.JSONEncoder.default(self.obj)
        except:
            return    




def getRoomImages(request):
    try:
        if request.method == 'GET' and 'room_id' in request.GET and request.GET['room_id'] != '':
            room_id = str(request.GET['room_id'])
            if room.objects.filter(room_id=room_id).exists():
                room_images = list(room_image.objects.filter(room=room.objects.get(room_id=room_id)).values_list())
                return JsonResponse(json.dumps({
                    "status" : True,
                    "msg" : "success",
                    "total": len(room_images),
                    "images" : room_images,
                }, cls=UUIDEncoder),safe=False)
            return JsonResponse(json.dumps({
                "status" : False,
                "msg" : "room-id not match",
            }), safe=False)    
    except Exception as err:
        print(err)        
    return JsonResponse(json.dumps({
        "status" : False,
        "msg" : "error",
    }), safe=False)




def roomDeatils(request):
    try:
        if request.method == 'GET' and 'room_id' in request.GET and request.GET['room_id'] != '':
            room_id = str(request.GET['room_id'])
            if room.objects.filter(room_id=room_id).exists():
                the_room = room.objects.get(room_id=room_id)
                room_images = list(room_image.objects.filter(room=the_room).values_list())
                return JsonResponse(json.dumps({
                    "status" : True,
                    "msg" : "success",
                    "total_images": len(room_images),
                    "images" : room_images,
                    "room_data" : the_room,
                }, cls=UUIDEncoder), safe=False)
            return JsonResponse(json.dumps({
                "status" : False,
                "msg" : "room-id not match",
            }), safe=False)    
    except Exception as err:
        print(err)        
    return JsonResponse(json.dumps({
        "status" : False,
        "msg" : "error",
    }), safe=False)



def getRooms(request):
    try:
        if request.method == 'GET':
            avl_rooms = room.objects.all()
            if 'q' in request.GET and request.GET['q'] != '':
                query = request.GET['q']
                avl_rooms = avl_rooms.filter(
                    Q(floor__icontains=query) | 
                    Q(gender_preference__icontains=query) |
                    Q(description__icontains=query) |
                    Q(room_type__icontains=query) |
                    Q(no_of_beds__icontains=query) | 
                    Q(max_occupants__icontains=query) | 
                    Q(current_occupants__icontains=query) | 
                    Q(room_rent__icontains=query) | 
                    Q(rent_type__icontains=query) | 
                    Q(appartment_name__icontains=query) | 
                    Q(appartment_address__icontains=query) | 
                    Q(manager__icontains=query)
                )
            avl_rooms = list(avl_rooms.values_list())
            return JsonResponse(json.dumps({
                "status" : True,
                "msg" : "success",
                "total" : len(avl_rooms),
                "rooms" : avl_rooms,
            }, cls=UUIDEncoder), safe=False)
    except Exception as err:
        print(err)        
    return JsonResponse(json.dumps({
        "status" : False,
        "msg" : "error",
    }), safe=False)

@login_required(login_url='/login')
def newAddRoom(request):
    if request.method == 'POST':
        try:
            form = AddRoomForm(request.POST or None)
            if form.is_valid():

                new_room = room.objects.create(
                    added_by = request.user.userprofile,
                    room_no = form.cleaned_data.get('room_no'),
                    floor = form.cleaned_data.get('floor'),
                    room_type = form.cleaned_data.get('room_type'),
                    appartment_name = form.cleaned_data.get('appartment_name'),
                    appartment_address = form.cleaned_data.get('appartment_address'),
                )

                if 'gender_preference' in request.POST and request.POST['gender_preference'] != '':
                    new_room.gender_preference = request.POST['gender_preference']

                if 'description' in request.POST and request.POST['description'] != '':
                    new_room.description = request.POST['description']

                if 'no_of_beds' in request.POST and request.POST['no_of_beds'] != '':
                    new_room.no_of_beds = request.POST['no_of_beds']

                if 'max_occupants' in request.POST and request.POST['max_occupants'] != '':
                    new_room.max_occupants = request.POST['max_occupants']

                if 'current_occupants' in request.POST and request.POST['current_occupants'] != '':
                    new_room.current_occupants = request.POST['current_occupants']

                if 'room_rent' in request.POST and request.POST['room_rent'] != '':
                    new_room.room_rent = request.POST['room_rent']

                if 'rent_type' in request.POST and request.POST['rent_type'] != '':
                    new_room.rent_type = request.POST['rent_type']

                if 'manager' in request.POST and request.POST['manager'] != '':
                    new_room.manager = request.POST['manager']                    

                if len(request.FILES) != 0:
                    for x in request.FILES.getlist('img') :
                        img_upload = room_image.objects.create(
                            room = new_room,
                            img = x
                        )
                        img_upload.save()
                new_room.save()
                messages.success(request, "Room added")
                return redirect(f'/rooms/room?room=True&room_id={new_room.room_id}')
            messages.error(request, "Fill all fields")
        except Exception as err:
            print(err)                  
    return render(request, 'room/add-room.html')    