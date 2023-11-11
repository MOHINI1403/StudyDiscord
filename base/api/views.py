from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer
@api_view(['GET'])
def getRouts(request):
    routes=[
        'GET/api',
        'GET /api/rooms',
        'GET /api/rooms/:id' # This will get the single object this would give the JSON response 
    ]
    return Response(routes) #Safe allows to convert python list into JSON List

@api_view(['GET'])
def getRooms(request):
    rooms=Room.objects.all()
    serializer=RoomSerializer(rooms,many=True) #many contains are we trying to seralise one object or many Python object 
    #SInce here we are seralizing querySet it is set to true
     
    #Response cannot return back Python objects List can be converted directly 
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request,pk):
    room=Room.objects.get(id=pk) #This will get the particular record 
    serializer=RoomSerializer(room,many=False) #many contains are we trying to seralise one object or many Python object 
    #Here many is false since it is going to return a single object 
     
    #Response cannot return back Python objects List can be converted directly 
    return Response(serializer.data)