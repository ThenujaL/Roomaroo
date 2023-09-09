from django.shortcuts import render
from django.http import JsonResponse


from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view()
def api_home(request):
    response_dict = {"messege" : "Welcome! This is the api home."}
    
    return Response(response_dict)


