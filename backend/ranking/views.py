from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CircuitSerialize, CircuitSerializer, RaceSerializer, DriverSerializer, EloDeltaSerializer
from .models import Race, Circuit, Driver, EloDelta


class CircuitView(viewsets.ModelViewSet):
    serializer_class = CircuitSerializer
    queryset = Circuit.objects.all()
