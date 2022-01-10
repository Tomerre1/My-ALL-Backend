from level.serializers import LevelSerializer
from level.models import Level
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def InsertLevel(request):
    serializer = LevelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateLevel(request):
    if request.method == 'PUT':
        try:
            level = Level.objects.get(levelNumber=request.data.get('levelNumber'))
        except Level.DoesNotExist:
            return Response('')
        serializer = LevelSerializer(level, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET'])
def getAllLevels(request):
    levels = Level.objects.all()
    serializer = LevelSerializer(levels, many=True)
    return Response(serializer.data)
    
@api_view(['DELETE'])
def deleteLevel(request):
    try:
        level = Level.objects.get(levelNumber=request.data.get('levelNumber'))
    except Level.DoesNotExist:
        return Response({'message': 'ERROR'})
    level.delete()
    return Response({'message': 'deleted successfuly'})
