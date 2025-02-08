import json
import os
import sys
import requests
import pytest
from jsonschema import validate
from config import BASE_URL
from tests.scema import roadster_schema
# Ensure config.py can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

def test_roadster():
    """Test to verify the SpaceX Roadster API response."""
    url = f"{config.BASE_URL}/roadster"
    response = requests.get(url)
    assert response.status_code == 200, "Failed to fetch roadster data."
    roadster = response.json()
    print(roadster)
    assert isinstance(roadster, dict), "Response should be a JSON object."
    required_fields = ["id", "name", "launch_date_utc", "earth_distance_km", "mars_distance_km"]
    for field in required_fields:
        assert field in roadster, f"Roadster object should have a '{field}' field."
    print("✅ SpaceX Roadster API Test Passed!")
    validate(instance=roadster,schema=roadster_schema)
    print("✅ JSON Schema Validation Passed for SpaceX Roadster!")

