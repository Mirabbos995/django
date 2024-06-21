from rest_framework import serializers
from .models import Person


class PoetSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    content = serializers.CharField()
    create_at = serializers.DateTimeField(read_only=True)
    update_at = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()


    def create(self, validated_data):
        return Person.objects.create(**validated_data)
