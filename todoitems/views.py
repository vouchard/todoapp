from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status, viewsets
from todoitems.serializers import TodoItemsSerializer,TodoCommentsSerializer
from todoitems.models import TodoComments,TodoItems

# Create your views here.
class TodoItemsView(viewsets.ModelViewSet):
    serializer_class =  TodoItemsSerializer
    queryset = TodoItems.objects.all()

class TodoCommentsView(viewsets.ModelViewSet):
    serializer_class = TodoCommentsSerializer
    queryset = TodoComments.objects.all()