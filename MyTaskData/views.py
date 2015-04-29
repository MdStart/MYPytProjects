from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from django.http import HttpResponse
from .models import MyData
from .serializers import TaskSerializer

permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

@api_view(['GET', 'POST'])
def task_list(request):

    """
    List all tasks, or create a new task.
    """
    if request.method == 'GET':
        tasks = MyData.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    """
    Get, udpate, or delete a specific task
    """
    try:
        task = MyData.objects.get(pk=pk)
    except MyData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.DATA)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

