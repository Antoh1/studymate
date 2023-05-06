from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Room, Message, Topic
from .forms import RoomForm
from django.db.models import Q

# rooms = [
#     {'id':1, 'name':'The art of python'},
#     {'id':2, 'name':'Jungle of Django'},
#     {'id':3, 'name':'The AI Revolution'},
# ]

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('study-home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "The user doesn't exist")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('study-home')
        else:
            messages.error(request, "Username OR Password doesn't exist")
    context = {'page':page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('study-home')


def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('study-home')
        else:
            messages.error(request, 'Error occured during registration')    
    return render(request, 'base/login_register.html', {'form':form})


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(host__username__icontains=q) | Q(name__icontains=q))
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms':rooms, 'topics':topics, 'room_count':room_count}
    return render(request, 'base/index.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    # for rm in rooms:
    #     if rm['id'] == int(pk):
    #         room = rm
    context = {'room': room}
    return render(request, 'base/room.html', context)

@login_required(login_url='study-login')
def create_room(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('study-home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)      

@login_required(login_url='study-login')
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.user != room.host:
        return HttpResponse("This action is restricted")
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid:
            form.save()
            return redirect('study-home')
    
    context = {'form': form}
    return render(request, 'base/room_form.html', context)  


@login_required(login_url='study-login')
def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse("This action is restricted")
    if request.method == "POST":
        room.delete()
        return redirect('study-home')
    
    return render(request, 'base/delete.html', {'obj': room})  
