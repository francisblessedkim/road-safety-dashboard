from rest_framework import serializers
from .models import TrafficAccident, Location, WeatherCondition, RoadCondition, AccidentCause

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class WeatherConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherCondition
        fields = '__all__'

class RoadConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadCondition
        fields = '__all__'

class AccidentCauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccidentCause
        fields = '__all__'

class TrafficAccidentSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    weather_condition = WeatherConditionSerializer()
    road_condition = RoadConditionSerializer()
    cause = AccidentCauseSerializer()

    class Meta:
        model = TrafficAccident
        fields = '__all__'

class TrafficAccidentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficAccident
        fields = '__all__'
