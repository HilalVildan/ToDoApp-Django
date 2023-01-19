from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet


from .models import Todo
from .serializers import TodoSerializer


# Create your views here.
def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to ApiTodo</h1></center>'
    )


@api_view(['GET', 'POST'])
def todo_list_create(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
       serializer = TodoSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def todo_get_del_upd(request, pk):

    todo = get_object_or_404(Todo, id=pk)

    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TodoSerializer(data=request.data, instance=todo)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)




######################## Concrete Views #################################


class Todos(ListCreateAPIView): # (get , post) ListCreateAPIView kenmdisi zaten tanimlamis o nedenle yazmiyoru
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetail(RetrieveUpdateDestroyAPIView): # (get, put, delete) RetrieveUpdateDestroyAPIView kenmdisi zaten tanimlamis o nedenle yazmiyoru
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


######################## ModelViewSet #################################


class TodoMVS(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

   
