from rest_framework import serializers
from rest_framework.response import Response

from .models import Person



class PoetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


# class PoetSerializers(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     create_at = serializers.DateTimeField(read_only=True)
#     update_at = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data): # validated_data - postmandan get qilib olingan malumot
#         return Person.objects.create(**validated_data) # ** - json dan dictga o'zgartirib databasega yozib qoyadi
#
#     def update(self, instance, validated_data): # instance - databasedagi malumot
#         instance.name = validated_data.get("name", instance.name) # "name" - yangilansin, instance.name - agar name yangilanmasa eskisi turaversin
#         instance.content = validated_data.get("content", instance.content)
#         instance.update_at = validated_data.get("update_at", instance.update_at)
#         instance.cat_id = validated_data.get("cat_id", instance.cat_id)
#         instance.save()
#         return instance



