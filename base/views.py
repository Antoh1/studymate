from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def room(request):
    return render(request, 'room.html')  
