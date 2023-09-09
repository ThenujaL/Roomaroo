from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse
from .models import Task

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, generics, permissions

from .serializers import TaskSerializer
from .permissions import IsStaffEditorPermission

# Create your views here. 

class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsStaffEditorPermission]

    def perform_create(self, serializer):
        # use this method to send a signal
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description') or None
        if description is None:
            description = title
        serializer.save(description=description)
    

task_ListCreate_View = TaskListCreateAPIView.as_view()

class TaskDetailAPIView(generics.RetrieveAPIView):
    queryset = Task.objects.all()  
    serializer_class = TaskSerializer
task_details_view = TaskDetailAPIView.as_view()


class TaskUpdateAPIView(generics.UpdateAPIView):
    queryset = Task.objects.all() 
    serializer_class = TaskSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        title = instance.title
        description = instance.description or None
        print(f'title : {title}, description: {description}')
        if description is None:
            instance.description = title
        instance.save()
task_update_view = TaskUpdateAPIView.as_view()

class TaskDestroyAPIView(generics.DestroyAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Task.objects.all() 
    serializer_class = TaskSerializer
    lookup_field = 'pk'
    
task_delete_view = TaskDestroyAPIView.as_view()


