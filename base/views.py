from django.shortcuts import render, redirect
from .models import Room, Message
from .forms import RoomForm

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

def create_room(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('study-home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)      

def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid:
            form.save()
            return redirect('study-home')
    
    context = {'form': form}
    return render(request, 'base/room_form.html', context)  


def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('study-home')
    
    return render(request, 'base/delete.html', {'obj': room})  
