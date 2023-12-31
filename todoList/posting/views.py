from django.shortcuts import render
from rest_framework.decorators import api_view
from posting.serializer import TaskSerializer
from rest_framework.response import Response

from .models import Task
# Create your views here.

# get 방식
@api_view(['GET'])
def getTaskList(request):
    TasksetQuery = Task.objects.all()
    serializer = TaskSerializer(TasksetQuery, many=True)
    print(serializer.data)
    return Response(serializer.data, status=200)


# get 방식이 아니라 Post 방식
@api_view(['POST'])
def addTask(request):
    # Post 방식인가?
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        # 만약 serializer가 유효한가, 멀쩡한가?
        if serializer.is_valid():
            # 저장
            serializer.save()
            # 반환
            return Response(serializer.data, status=200)
        else:
            # 아니면 에러 출력
            print(serializer.errors)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def updateTask(request, pk, work):
    # id로 해당하는 태스크를 가져오기
    targetTask = Task.objects.get(id=pk)
    targetTask.work = work
    targetTask.isComplete = False
    targetTask.save()

    # targetTask를 직렬화
    serialized_Task = TaskSerializer(targetTask)
    return Response(serialized_Task.data, status=200)


@api_view(['GET'])
def removeTask(request, pk):
    # id로 해당하는 태스크를 가져오기
    Task.objects.get(id=pk).delete()
    # 빈 내용이지만 반환하기
    return Response(status=200)