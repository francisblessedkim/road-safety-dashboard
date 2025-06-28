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
    # Resolve the absolute path to the CSV file using Django's BASE_DIR
    csv_path = Path(settings.BASE_DIR) / relative_csv_path

    # Open the CSV file for reading
    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Parse city and country from the 'Location' column
            city_country = row["Location"].split(",")
            city = city_country[0].strip()
            country = city_country[1].strip() if len(city_country) > 1 else ""

            # Get or create a Location object
            location, _ = Location.objects.get_or_create(
                city=city,
                country=country,
                latitude=float(row["Latitude"]),
                longitude=float(row["Longitude"]),
            )

            # Get or create a WeatherCondition object
            weather, _ = WeatherCondition.objects.get_or_create(
                description=row["Weather Condition"].strip()
            )

            # Get or create a RoadCondition object
            road, _ = RoadCondition.objects.get_or_create(
                description=row["Road Condition"].strip()
            )

            # Get or create an AccidentCause object
            cause, _ = AccidentCause.objects.get_or_create(
                description=row["Cause"].strip()
            )

            # Parse date and time fields
            date = datetime.strptime(row["Date"], "%Y-%m-%d").date()
            time = datetime.strptime(row["Time"], "%H:%M").time()

            # Create or update a TrafficAccident record with the parsed data
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
