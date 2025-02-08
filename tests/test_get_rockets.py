import json
import os
import sys
import requests
import pytest
from jsonschema import validate

from tests.scema import rocket_schema

# Ensure config.py can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config
from scema import launch_schema
def test_get_rockets():
    """Test to verify the SpaceX rockets API endpoint."""
    url = f"{config.BASE_URL}/rockets"
    response = requests.get(url)
    assert response.status_code == 200, "Failed to fetch rockets."
    rockets = response.json()  # Convert API response to JSON
    print(json.dumps(rockets[0], indent=4))  # Print response for debugging
    assert isinstance(rockets, list), "Response should be a list of rockets."
    assert len(rockets) > 0, "No rockets found."
    # Validate the first rocket entry
    if rockets:
        assert "id" in rockets[0], "Rocket object should have an 'id' field."
        assert "name" in rockets[0], "Rocket object should have a 'name' field."
        assert "active" in rockets[0], "Rocket object should have an 'active' field."
    print("✅ Rocket details test passed!")
    validate(instance=rockets, schema=rocket_schema)
    print("✅ JSON Schema Validation Passed!")


