from django.shortcuts import render
from .models import Room

#rooms = [
#    {'id': 1, 'name': 'Champions League'},
#    {'id': 2, 'name': 'Premier League'},
#    {'id': 3, 'name': 'La Liga'},
#    {'id': 4, 'name': 'Serie A'},
#    {'id': 5, 'name': 'Bundesliga'},
#]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'baza/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'baza/room.html', context)

def createRoom(request):

    context = {}
    return render(request, 'baza/room_form.html', context)
