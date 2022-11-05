from django.shortcuts import render
from .models import Artiste, Song
from .serializers import ArtisteSerializer, SongSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
# Create your views here

@api_view(["GET", 'POST'])
def ArtisteView(request):
    if request.method == "GET":
        Artistes = Artiste.objects.all()
        serializer = ArtisteSerializer(Artistes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': 
        serializer = ArtisteSerializer(data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        


@api_view(['GET', 'PUT', 'DELETE'])
def Artistes_detail(request, pk):

    try:
        Artistes = Artiste.objects.get(pk=pk)
    except Artistes.DoesNotExist:
        return Response(status=404)


    if request.method == 'GET':
        serializer = ArtisteSerializer(Artistes)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArtisteSerializer(Artiste, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Artiste.delete()
        return Response(status=204)


class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer 



         

