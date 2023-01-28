from django.shortcuts import render
from django.http import HttpResponse


def see_all_rooms(request):
    return HttpResponse("Hello World")


def see_one_room(request, room_id):
    return HttpResponse(f"Hello World {room_id}")
