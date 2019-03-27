from django.http import JsonResponse, HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from api.models import Word, Video
from api.serializers import WordSerializer, VideoSerializer


@api_view(['GET', 'POST'])
def word_list(request):
    if request.method == 'GET':
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def word_detail(request, pk):
    try:
        word = Word.objects.get(pk=pk)
    except Word.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WordSerializer(word)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WordSerializer(word, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def video_list(request, pk):
    try:
        word = Word.objects.get(pk=pk)
    except Word.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        videos = word.get_all_videos()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
