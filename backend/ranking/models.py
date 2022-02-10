from django.db import models
from django.conf import settings


class Driver(models.Model):
    id = models.IntegerField(primary_key=True)
    # String to differentiate drivers
    driverRef = models.CharField(max_length=30)
    # Not all drivers have numbers
    number = models.IntegerField(blank=True, null=True)
    # Not all drivers have codes
    code = models.CharField(
        max_length=3, blank=True, null=True)
    forename = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    dob = models.DateField()
    nationality = models.CharField(max_length=30)
    url = models.URLField()
    elo = models.PositiveIntegerField(
        default=getattr(settings, "STARTING_ELO"))

    def __str__(self):
        return f'<Driver {self.id}>'

    def ChangeRating(self, race, elo):
        delta = EloDelta(self, race, self.elo, elo)
        delta.save()
        self.elo = elo
        self.save()


class Circuit(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    circuitRef = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    lat = models.DecimalField(decimal_places=6, max_digits=10)
    lng = models.DecimalField(decimal_places=6, max_digits=10)
    alt = models.IntegerField()
    url = models.URLField()

    def __str__(self):
        return f'<Circuit {self.id}>'


class Race(models.Model):
    id = models.IntegerField(primary_key=True)
    # probably shouldn't be an int field
    year = models.IntegerField()
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()
    url = models.URLField(blank=True)
    drivers = models.ManyToManyField(Driver, through="RaceResult", blank=True)

    def __str__(self):
        return f'<Race {self.id}>'

    def addDriversAndResults(self, resultArray):
        # resultArray = [(driver, positionInteger), ...]
        for driver, position in resultArray:
            result = RaceResult(driver=driver, race=self, position=position)
            result.save()


class RaceResult(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    position = models.IntegerField()


class EloDelta(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    startingElo = models.PositiveIntegerField()
    endingElo = models.PositiveIntegerField()

    def __init__(self, driver, race, startingElo, endingElo):
        self.driver = driver
        self.race = race
        self.startingElo = startingElo
        self.endingElo = endingElo
        self.save()

    def __str__(self) -> str:
        return f'<EloDelta {self.driverId + "-" + self.raceId}>'
