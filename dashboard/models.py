from django.db import models  # Import Django's model base classes


class Location(models.Model):
    city = models.CharField(max_length=100)  # Name of the city where the location is
    country = models.CharField(max_length=100)  # Country of the location
    latitude = models.FloatField()  # Latitude coordinate of the location
    longitude = models.FloatField()  # Longitude coordinate of the location

    def __str__(self):
        return f"{self.city}, {self.country}"  # String representation for admin and shell


class WeatherCondition(models.Model):
    description = models.CharField(max_length=50, unique=True)  # Description of weather (e.g., Rainy, Sunny)

    def __str__(self):
        return self.description  # String representation


class RoadCondition(models.Model):
    description = models.CharField(max_length=50, unique=True)  # Description of road condition (e.g., Wet, Dry)

    def __str__(self):
        return self.description  # String representation


class AccidentCause(models.Model):
    description = models.CharField(max_length=100, unique=True)  # Description of accident cause (e.g., Speeding)

    def __str__(self):
        return self.description  # String representation


class TrafficAccident(models.Model):
    accident_id = models.CharField(max_length=20, unique=True)  # Unique identifier for the accident
    date = models.DateField()  # Date when the accident occurred
    time = models.TimeField()  # Time when the accident occurred
    location = models.ForeignKey(Location, on_delete=models.CASCADE)  # Reference to the accident location
    weather_condition = models.ForeignKey(
        WeatherCondition, on_delete=models.SET_NULL, null=True  # Reference to weather condition, nullable
    )
    road_condition = models.ForeignKey(
        RoadCondition, on_delete=models.SET_NULL, null=True  # Reference to road condition, nullable
    )
    cause = models.ForeignKey(AccidentCause, on_delete=models.SET_NULL, null=True)  # Reference to accident cause, nullable
    vehicles_involved = models.PositiveIntegerField()  # Number of vehicles involved in the accident
    casualties = models.PositiveIntegerField()  # Number of casualties in the accident

    def __str__(self):
        return f"{self.accident_id} - {self.location}"  # String representation
