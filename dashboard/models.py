from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.city}, {self.country}"


class WeatherCondition(models.Model):
    description = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.description


class RoadCondition(models.Model):
    description = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.description


class AccidentCause(models.Model):
    description = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.description


class TrafficAccident(models.Model):
    accident_id = models.CharField(max_length=20, unique=True)
    date = models.DateField()
    time = models.TimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    weather_condition = models.ForeignKey(
        WeatherCondition, on_delete=models.SET_NULL, null=True
    )
    road_condition = models.ForeignKey(
        RoadCondition, on_delete=models.SET_NULL, null=True
    )
    cause = models.ForeignKey(AccidentCause, on_delete=models.SET_NULL, null=True)
    vehicles_involved = models.PositiveIntegerField()
    casualties = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.accident_id} - {self.location}"
