from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Person
from .serializers import PoetSerializers


class ListPoet(APIView):
    def get(self, request): # request - postmanga bervorilyatgan parametr
        lst = Person.objects.all()
        return Response({'Poet': PoetSerializers(lst, many=True).data})

    def post(self, requests):
        serializers = PoetSerializers(data=requests.data)      #request.data - postmandaagi name,cat_id lar requestlar deyiladi
        serializers.is_valid(raise_exception=True)
        serializers.save()  # databasega saqlash uchun save() yozilgan

        return Response({"posts": serializers.data})

class UpdateDelete(APIView):
    def put(self, requests, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response({"post": "Method PUT not allowed!"})

        try:
            instance = Person.objects.get(pk=pk)
        except:
            return Response({"post": "Object not found!"})

        serializers = PoetSerializers(data=requests.data, instance=instance)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({"post": serializers.data})


    def patch(self, requests, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"post": "Method PUT not allowed!"})

        try:
            instance = Person.objects.get(pk=pk)
        except:
            return Response({"post": "Object not found!"})

        serializers = PoetSerializers(data=requests.data, instance=instance, partial=True)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({"post": serializers.data})


    def delete(self, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"post": "Method PUT not allowed!"})
        try:
            instance = Person.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({"post": "Object not found!"})

        return Response({"answer": f"Deleted ID - {pk}"})

