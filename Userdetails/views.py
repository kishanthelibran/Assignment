from django.shortcuts import render
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from django.http import HttpResponse


@api_view(['POST'])
def RegisterUser(request):
    return Response('Success')
