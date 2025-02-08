import json
import os
import sys
import requests
import pytest
from jsonschema import validate
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config
from scema import launch_schema  # Import the defined schema

def test_get_launches_latest_upcoming():
    url = f"{config.BASE_URL}/launches/upcoming"
    response = requests.get(url)
    assert response.status_code == 200, "Failed to fetch launches."
    launches = response.json()  # API response as JSON
    print(launches[0]["fairings"])
    assert isinstance(launches, list), "Response should be a list."
    # Validate the first launch entry against the schema
    #assert condition, "Error message(optional)"
    '''assert is a built-in Python statement that is used to check if a condition is true.
       If the condition is false,  
       the program stops and throws an AssertionError'''
    if launches:  # Check only if launches exist
        assert "id" in launches[0], "Launch object should have an 'id' field."
        assert "name" in launches[0], "Launch object should have a 'name' field."
        assert "date_utc" in launches[0], "Launch object should have a 'date_utc' field."

    print("✅ Upcoming Launches API Test Passed!")
