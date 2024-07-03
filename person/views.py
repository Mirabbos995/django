from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Person, Category
from .serializers import PoetSerializers






class CRUDPoet(mixins.CreateModelMixin,         # These are Model View Sets
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    # queryset = Person.objects.all()
    serializer_class = PoetSerializers

    def get_queryset(self):
        return Person.objects.all()

    @action(detail=False, methods=['get']) # action - We can access the data through a single url, and this is done by an 'action'
    def category(self, request):
        data = Category.objects.all()  # get(pk=pk) - 'pk' returns one specific data
        return Response({"data": [x.name for x in data]})               # x.name - there is id and name in database
                                                                        # and we'll get only name not id





# Shorter option of CRUD 👇




# class GetnAllPoet(generics.ListAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PoetSerializers
#
# class GetOnePoet(generics.RetrieveAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PoetSerializers
#
# class PostPoet(generics.CreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PoetSerializers
#
# class UpdatePoet(generics.UpdateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PoetSerializers
#
# class DeletePoet(generics.DestroyAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PoetSerializers








# Spreaded option of CRUD👇



# class GetPoet(APIView):
#     def get(self, request, **kwargs): # request - postmanga bervorilyatgan parametr
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"post": "Method PUT not allowed!"})
#         try:
#             instance = Person.objects.get(pk=pk)
#         except:
#             return Response({"post": "Object not found!"})
#         serializer = PoetSerializers(instance)
#         return Response({'post': serializer.data})
#
#
# class ListPoet(APIView):
#     def post(self, requests):
#         serializers = PoetSerializers(data=requests.data)      #request.data - postmandaagi name,cat_id lar requestlar deyiladi
#         serializers.is_valid(raise_exception=True)
#         serializers.save()  # databasega saqlash uchun save() yozilgan
#
#         return Response({"posts": serializers.data})
#
# class UpdateDelete(APIView):
#     def put(self, requests, *args, **kwargs):  # "kwargs" URL namunasidan asosiy kalitni ("pk") olish
#                                                 # va yuklash uchun ishlatiladi, bu esa "put"
#                                                  # usuliga ma'lumotlar bazasidagi mos ob'ektni yangilash imkonini beradi.
#         pk = kwargs.get("pk", None)  # None - pk topilmidigan bo'lsa None qaytarsin!
#
#         if not pk: # agar pk yo'q bolsa if ishlaydi
#             return Response({"post": "Method PUT not allowed!"})
#
#         try:
#             instance = Person.objects.get(pk=pk)
#         except:
#             return Response({"post": "Object not found!"})
#
#         serializers = PoetSerializers(data=requests.data, instance=instance) # (data=requests.data) - postmandagi bervorilgan data va instance=instance / put ga o'zgaradi
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response({"post": serializers.data}) # serializers.data - update bogan data qaytadi
#
#
#     def patch(self, requests, *args, **kwargs): # put zapros - toliq hammasi o'zgartirilishi kerak, patch zapros - bittasni ozgartirsa boladi
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"post": "Method PUT not allowed!"})
#
#         try:
#             instance = Person.objects.get(pk=pk)
#         except:
#             return Response({"post": "Object not found!"})
#
#         serializers = PoetSerializers(data=requests.data, instance=instance, partial=True)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response({"post": serializers.data})
#
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"post": "Method PUT not allowed!"})
#         try:
#             instance = Person.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({"post": "Object not found!"})
#
#         return Response({"answer": f"Deleted ID - {pk}"})
#
#
