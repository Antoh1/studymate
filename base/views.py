from django.shortcuts import render
from .models import Room

# rooms = [
#     {'id':1, 'name':'The art of python'},
#     {'id':2, 'name':'Jungle of Django'},
#     {'id':3, 'name':'The AI Revolution'},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/index.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    # for rm in rooms:
    #     if rm['id'] == int(pk):
    #         room = rm
    context = {'room': room}
    return render(request, 'base/room.html', context)  
