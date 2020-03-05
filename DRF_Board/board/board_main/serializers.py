from .models import Boardlist
from rest_framework import serializers

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boardlist
        fields = '__all__'


class BoardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boardlist
        fields = ('id', 'title', 'content', 'date','priority')

class BoardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boardlist
        fields = ('title', 'content', 'date','priority')      