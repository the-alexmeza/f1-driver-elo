from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CircuitSerializer, RaceSerializer, DriverSerializer, EloDeltaSerializer
from .models import Race, Circuit, Driver, EloDelta


class CircuitView(viewsets.ModelViewSet):
    serializer_class = CircuitSerializer
    queryset = Circuit.objects.all()


class DriverView(viewsets.ModelViewSet):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all().order_by('-elo')


class RaceView(viewsets.ModelViewSet):
    serializer_class = RaceSerializer
    queryset = Race.objects.all()


class EloDeltaView(viewsets.ModelViewSet):
    serializer_class = EloDeltaSerializer
    queryset = EloDelta.objects.all()
