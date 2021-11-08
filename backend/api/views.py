from django.shortcuts import render
from .serializers import RoomSerializer
from .models import Room
from rest_framework.generics import CreateAPIView, ListAPIView
# Create your views here.

class RoomView(ListAPIView):
	queryset = Room.objects.all()
	serializer_class = RoomSerializer