from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import CityList
from . serializers import CityListSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
import requests
# Create your views here.
class Indiancitylist(APIView):

    #authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        city1 = CityList.objects.all()
        serializer = CityListSerializer(city1, many = True)
        return Response(serializer.data)

    def post(self, request):
        #data = JSONParser().parse(request)
        serializer = CityListSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)


class City_Detail(APIView):
    
    def get_object(self, id):
        try:
            return CityList.objects.get(id=id)
        
        except CityList.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        city = self.get_object(id)
        serializer = CityListSerializer(city)
        return Response(serializer.data)

    def post(self, request, id):
        city = self.get_object(id)
        serializer = CityListSerializer(city,data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        city = self.get_object(id)
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def index(request):
    return render(request, 'india/index.html')
    
