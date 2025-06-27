from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Location, WeatherCondition, RoadCondition, AccidentCause, TrafficAccident
from datetime import date, time


class TrafficAccidentAPITest(APITestCase):
    def setUp(self):
        # Create related objects
        self.location = Location.objects.create(city="Test City", country="Testland", latitude=0.0, longitude=0.0)
        self.weather = WeatherCondition.objects.create(description="Clear")
        self.road = RoadCondition.objects.create(description="Dry")
        self.cause = AccidentCause.objects.create(description="Speeding")

        # Create a sample accident
        self.accident = TrafficAccident.objects.create(
            accident_id="TST123",
            date=date(2025, 6, 20),
            time=time(12, 0),
            location=self.location,
            weather_condition=self.weather,
            road_condition=self.road,
            cause=self.cause,
            vehicles_involved=2,
            casualties=1
        )

    def test_get_all_accidents(self):
        response = self.client.get('/api/accidents/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data['results']), 1)

    def test_filter_by_city(self):
        response = self.client.get('/api/accidents/by-city/?city=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data['results']), 1)

    def test_post_create_accident(self):
        data = {
            "accident_id": "POST123",
            "date": "2025-06-20",
            "time": "15:30:00",
            "location": self.location.id,
            "weather_condition": self.weather.id,
            "road_condition": self.road.id,
            "cause": self.cause.id,
            "vehicles_involved": 3,
            "casualties": 2
        }
        response = self.client.post('/api/accidents/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
