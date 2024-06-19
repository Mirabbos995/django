from django.shortcuts import render
from rest_framework import generics
from .models import Person
from .serializers import PoesSerializers
# Create your views here.
class ListPoet(generics.GenericAPIView):
    queryset = Person.objects.all()
    serializer_class = PoesSerializers