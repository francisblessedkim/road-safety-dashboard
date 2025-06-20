from django.shortcuts import render
from rest_framework import generics
from .models import TrafficAccident
from .serializers import TrafficAccidentSerializer
from .serializers import TrafficAccidentCreateSerializer
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view

class TrafficAccidentListView(generics.ListAPIView):
    queryset = TrafficAccident.objects.all()
    serializer_class = TrafficAccidentSerializer

class FilterByCityView(generics.ListAPIView):
    serializer_class = TrafficAccidentSerializer

    def get_queryset(self):
        city = self.request.query_params.get('city')
        if city:
            return TrafficAccident.objects.filter(location__city__icontains=city)
        return TrafficAccident.objects.none()

class FilterByCauseView(generics.ListAPIView):
    serializer_class = TrafficAccidentSerializer

    def get_queryset(self):
        cause = self.request.query_params.get('cause')
        if cause:
            return TrafficAccident.objects.filter(cause__description__icontains=cause)
        return TrafficAccident.objects.none()

class TrafficAccidentCreateView(generics.CreateAPIView):
    queryset = TrafficAccident.objects.all()
    serializer_class = TrafficAccidentCreateSerializer