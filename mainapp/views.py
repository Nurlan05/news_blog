from django.shortcuts import render
from mainapp.models import News
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NewsSerializers,NewsCreateSerializers


@api_view(['GET'])
def index(request):
    news = News.objects.all()
    serializer = NewsSerializers(news, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def newsDetail(request, pk):
    news = News.objects.get(id=pk)
    serializer = NewsSerializers(news, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def newsCreate(request):
    serializer = NewsCreateSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def newsUpdate(request, pk):
    news = News.objects.get(id=pk)
    serializer = NewsCreateSerializers(instance=news, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def newsDelete(request, pk):
    news = News.objects.get(id=pk)
    news.delete()
    return Response("Successfully deleted!")
