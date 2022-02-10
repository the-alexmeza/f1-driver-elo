from rest_framework import serializers
from .models import Race, Driver, Circuit, EloDelta


class CircuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circuit
        fields = ('id', 'circuitRef', 'name', 'location',
                  'country', 'lat', 'lng', 'alt', 'url')


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'driverRef', 'number', 'code', 'forename',
                  'surname', 'dob', 'nationality', 'url', 'elo')


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ('id', 'year', 'circuit', 'name', 'date', 'url', 'drivers')


class EloDeltaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EloDelta
        fields = ('driver', 'race', 'startingElo', 'endingElo')
