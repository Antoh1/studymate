from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = ['Get api/rooms/','GET api/rooms/:id','GET api/']
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)        

# from django.http import JsonResponse
# def getRoutes(request):
#     routes = ['Get api/rooms/','GET api/rooms/:id','GET api/']
#     return JsonResponse(routes, safe=False)    