from django.shortcuts import render
from rest_framework import generics
from .models import TrafficAccident
from .serializers import TrafficAccidentSerializer
from .serializers import TrafficAccidentCreateSerializer
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime


def api_home(request):
    return render(request, "api_home.html")


class TrafficAccidentListView(generics.ListAPIView):
    queryset = TrafficAccident.objects.all()
    serializer_class = TrafficAccidentSerializer


class FilterByCityView(generics.ListAPIView):
    serializer_class = TrafficAccidentSerializer

    def get_queryset(self):
        city = self.request.query_params.get("city")
        if city:
            return TrafficAccident.objects.filter(location__city__icontains=city)
        return TrafficAccident.objects.none()


class FilterByCauseView(generics.ListAPIView):
    serializer_class = TrafficAccidentSerializer

    def get_queryset(self):
        cause = self.request.query_params.get("cause")
        if cause:
            return TrafficAccident.objects.filter(cause__description__icontains=cause)
        return TrafficAccident.objects.none()


class TrafficAccidentCreateView(generics.CreateAPIView):
    queryset = TrafficAccident.objects.all()
    serializer_class = TrafficAccidentCreateSerializer


class FilterMultipleView(generics.ListAPIView):
    serializer_class = TrafficAccidentSerializer

    def get_queryset(self):
        queryset = TrafficAccident.objects.all()
        city = self.request.query_params.get("city")
        cause = self.request.query_params.get("cause")

        if city:
            queryset = queryset.filter(location__city__icontains=city)
        if cause:
            queryset = queryset.filter(cause__description__icontains=cause)

        return queryset


class WeekendAccidentView(generics.ListAPIView):
    serializer_class = TrafficAccidentSerializer

    def get_queryset(self):
        queryset = TrafficAccident.objects.all()
        weekend_accidents = []

        for accident in queryset:
            if accident.date.weekday() in [5, 6]:  # Saturday = 5, Sunday = 6
                weekend_accidents.append(accident.id)

        return queryset.filter(id__in=weekend_accidents)
