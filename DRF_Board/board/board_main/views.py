from django.shortcuts import render
from .models import Boardlist
from .serializers import BoardSerializer, BoardDetailSerializer, BoardCreateSerializer

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
# Create your views here.

class Board_main(ListAPIView):
    ordering_fields='date'
    queryset=Boardlist.objects.all()
    serializer_class = BoardSerializer

class Board_detail(RetrieveAPIView):
    lookup_field='id'
    queryset=Boardlist.objects.all()
    serializer_class = BoardDetailSerializer

class Board_update(UpdateAPIView):
    lookup_field='id'
    queryset=Boardlist.objects.all()
    serializer_class = BoardDetailSerializer

class Board_delete(DestroyAPIView):
    lookup_field='id'
    queryset=Boardlist.objects.all()
    serializer_class = BoardDetailSerializer

class Board_create(CreateAPIView):
    queryset=Boardlist.objects.all()
    serializer_class = BoardCreateSerializer