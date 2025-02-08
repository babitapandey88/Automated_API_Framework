import json
import os
import sys
import requests
import pytest
from jsonschema import validate
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config
from scema import launch_schema  # Import the defined schema

def test_get_launches_latest():
    url = f"{config.BASE_URL}/launches/latest"
    response = requests.get(url)
    print(json.dumps(response.json(), indent=4))  # Print only the first launch for readability
    assert response.status_code == 200, "Failed to fetch launches."
    launches = response.json()  # API response as JSON
    print(launches)
    assert isinstance(launches, dict), "Response should be a list."
    # Validate the first launch entry against the schema
    validate(instance=launches, schema=launch_schema)
    print("✅ JSON Schema Validation Passed!")
