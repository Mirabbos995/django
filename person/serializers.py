from rest_framework import serializers

from .models import Person


class PoesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'content')