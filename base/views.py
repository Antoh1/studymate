from django.shortcuts import render

rooms = [
    {'id':1, 'name':'The art of python'},
    {'id':2, 'name':'Jungle of Django'},
    {'id':3, 'name':'The AI Revolution'},
]

def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/index.html', context)

def room(request):
    return render(request, 'base/room.html')  
