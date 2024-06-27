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
    def put(self, requests, *args, **kwargs): #   ushbu kontekstdagi "kwargs" URL namunasidan
                                                 # asosiy kalitni ("pk") olish va yuklash uchun ishlatiladi, bu esa "put"
                                                 # usuliga ma'lumotlar bazasidagi mos ob'ektni yangilash imkonini beradi.
        pk = kwargs.get("pk", None) # None - pk topilmidigan bo'lsa None qaytarsin!

        if not pk: # agar pk yo'q bolsa if ishlaydi
            return Response({"post": "Method PUT not allowed!"})

        try:
            instance = Person.objects.get(pk=pk)
        except:
            return Response({"post": "Object not found!"})

        serializers = PoetSerializers(data=requests.data, instance=instance) # (data=requests.data) - postmandagi bervorilgan data va instance=instance / put ga o'zgaradi
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({"post": serializers.data}) # serializers.data - update bogan data qaytadi


    def patch(self, requests, *args, **kwargs): # put zapros - toliq hammasi o'zgartirilishi kerak, patch zapros - bittasni ozgartirsa boladi
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

