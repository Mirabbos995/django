from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Person
from .serializers import PoetSerializers

# Create your views here.
class ListPoet(APIView):
    def get(self, request):
        respond = Person.objects.all().values()
        return Response({'Lier': PoetSerializers(respond, many=True).data})

    def post(self, requests):
        serializers = PoetSerializers(data=requests.data)
        serializers.is_valid(raise_exception=True)
        posts = Person.objects.create(
            name=requests.data["name"],
            content=requests.data["content"],
            cat_id=requests.data["cat_id"],
        )

        return Response({"posts": PoetSerializers(posts).data})


# class ListPoet(generics.ListAPIView):
#     queryset = Person.objects.all().values()
#     serializer_class = PoetSerializers
