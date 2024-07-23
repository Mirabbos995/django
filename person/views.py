from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Person, Category
from .permission import IsOwnerOrReadOnly
# from .permission import IsAdminUserOrReadOnly, IsOwnerUserOrReadOnly
from .serializers import PoetSerializers






class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    # queryset = Person.objects.all()
    serializer_class = PoetSerializers

    def get_queryset(self):   # 'get_queryset' should always contain 'basename'
        pk = self.kwargs.get("pk")
        if not pk:
            return Person.objects.all()[:3]

        return Person.objects.filter(pk=pk)
        # return Person.objects.all()[:3]   # [:3] - is restriction (no more than 3 data)

    @action(detail=False, methods=['get']) # action - We can access the data through a single url + 'category' url added, and this is done by an 'action'
    def category(self, request):
        data = Category.objects.all()  # pk=pk - 'pk' returns one specific data
        return Response({"data": [x.name for x in data]})               # x.name - there is 'id' and 'name' in database
                                                                        # and we'll get only name not id







# Shorter option of CRUD 👇

# class PoetPagination(PageNumberPagination):   # always used in List!
#     page_size = 1
#     page_size_query_param = 'page_size'
#     max_page_size = 10000

#
# class ListCreatePoet(generics.ListCreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PoetSerializers
#     permission_classes = [IsAuthenticated]   # This is only for those who logged in
#     # authentication_classes = (TokenAuthentication, )
#     # pagination_class = PoetPagination
#
# class UpdataPoet(generics.UpdateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PoetSerializers
#     permission_classes = (IsOwnerOrReadOnly, )      # O'chiroladigan faqat admin bo'lishi kerak
#
#
# class DeleteRetrivePoet(generics.RetrieveDestroyAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PoetSerializers
#     permission_classes = (IsAuthenticated, )     # Users can read but cannot delete
#                             #IsAuthenticatedOrReadOnly,


# class GetAllPoet(generics.ListCreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PoetSerializers
#     # permission_classes = [IsAuthenticated]
#
# class UpdatePoet(generics.UpdateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PoetSerializers
#     # permission_classes = (IsOwnerOrReadOnly, )
#
# class DeletePoet(generics.RetrieveDestroyAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PoetSerializers
#     permission_classes = (IsAuthenticatedOrReadOnly,)

                            #IsAdminUser - users can see nothing


# Spreaded option of CRUD👇

# class GetPoet(APIView):
#     def get(self, request):
#         a = Person.objects.all()
#         return Response({'Poet': PoetSerializers(a, many=True).data})
#
#     def post(self, request):
#         serializers = PoetSerializers(data=request.data)   #request.data - postmandaagi name,cat_id lar requestlar deyiladi
#         serializers.is_valid(raise_exception=True)
#         serializers.save()          # databasega saqlash uchun save() yozilgan
#
#         return Response({"posts": serializers.data})
#
#     def put(self, requests, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"post": "Method put not allowed"})
#         try:
#             instance = Person.objects.get(pk=pk)
#         except:
#             return Response({"post": "Object not found"})
#
#         serializers = PoetSerializers(data=requests.data, instance=instance)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response({"post": serializers.data})
#
#     def patch(self, requests, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"post": "Method put not allowed"})
#         try:
#             instance = Person.objects.get(pk=pk)
#         except:
#             return Response({"post": "Object not found"})
#
#         serializers = PoetSerializers(data=requests.data, instance=instance, partial=True)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response({"post": serializers.data})
#     def delete(self, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"post": "Method put not allowed"})
#         try:
#             instance = Person.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({"post": "Object not found!"})
#
#         return Response({"answer": f"Deleted ID - {pk}"})


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















