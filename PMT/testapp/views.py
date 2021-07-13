from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView
from testapp.serializers import ClientSerializer,ProjectSerializer
from testapp.models import Client,Project

class CreateClientAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ListClientAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class UpdateClientAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer



class DeleteClientAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class CreateProjectAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ListProjectAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
