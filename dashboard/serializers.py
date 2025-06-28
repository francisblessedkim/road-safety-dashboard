from rest_framework import serializers
from .models import (
    TrafficAccident,
    Location,
    WeatherCondition,
    RoadCondition,
    AccidentCause,
)

# Serializer for the Location model
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"  # Serialize all fields of Location

# Serializer for the WeatherCondition model
class WeatherConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherCondition
        fields = "__all__"  # Serialize all fields of WeatherCondition

# Serializer for the RoadCondition model
class RoadConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadCondition
        fields = "__all__"  # Serialize all fields of RoadCondition

# Serializer for the AccidentCause model
class AccidentCauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccidentCause
        fields = "__all__"  # Serialize all fields of AccidentCause

# Serializer for the TrafficAccident model with nested serializers for related fields
class TrafficAccidentSerializer(serializers.ModelSerializer):
    location = LocationSerializer()  # Nested serializer for Location
    weather_condition = WeatherConditionSerializer()  # Nested serializer for WeatherCondition
    road_condition = RoadConditionSerializer()  # Nested serializer for RoadCondition
    cause = AccidentCauseSerializer()  # Nested serializer for AccidentCause

    class Meta:
        model = TrafficAccident
        fields = "__all__"  # Serialize all fields of TrafficAccident

# Serializer for creating TrafficAccident instances (uses primary keys for related fields)
class TrafficAccidentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficAccident
        fields = "__all__"  # Serialize all fields for creation
