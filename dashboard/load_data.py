import csv
from datetime import datetime
from pathlib import Path
from django.conf import settings
from dashboard.models import (
    Location,
    WeatherCondition,
    RoadCondition,
    AccidentCause,
    TrafficAccident,
)


def load_traffic_data(relative_csv_path="data/global_traffic_accidents.csv"):
    # Resolve path using BASE_DIR from settings
    csv_path = Path(settings.BASE_DIR) / relative_csv_path

    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            city_country = row["Location"].split(",")
            city = city_country[0].strip()
            country = city_country[1].strip() if len(city_country) > 1 else ""

            location, _ = Location.objects.get_or_create(
                city=city,
                country=country,
                latitude=float(row["Latitude"]),
                longitude=float(row["Longitude"]),
            )

            weather, _ = WeatherCondition.objects.get_or_create(
                description=row["Weather Condition"].strip()
            )

            road, _ = RoadCondition.objects.get_or_create(
                description=row["Road Condition"].strip()
            )

            cause, _ = AccidentCause.objects.get_or_create(
                description=row["Cause"].strip()
            )

            date = datetime.strptime(row["Date"], "%Y-%m-%d").date()
            time = datetime.strptime(row["Time"], "%H:%M").time()

            TrafficAccident.objects.update_or_create(
                accident_id=row["Accident ID"],
                defaults={
                    "date": date,
                    "time": time,
                    "location": location,
                    "weather_condition": weather,
                    "road_condition": road,
                    "cause": cause,
                    "vehicles_involved": int(row["Vehicles Involved"]),
                    "casualties": int(row["Casualties"]),
                },
            )
