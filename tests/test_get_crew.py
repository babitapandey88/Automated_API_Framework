import json
import os
import sys
import requests
import pytest
from jsonschema import validate
# Ensure config.py can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config
def test_get_crew():
    """Test to verify the SpaceX crew API endpoint."""
    url = f"{config.BASE_URL}/crew"
    response = requests.get(url)
    assert response.status_code == 200, "Failed to fetch crew details."
    crew_members = response.json()  # Convert API response to JSON
    print(json.dumps(crew_members, indent=4))  # Print response for debugging
    assert isinstance(crew_members, list), "Response should be a list of crew members."
    assert len(crew_members) > 0, "No crew members found."
    # Validate the first crew member entry
    if crew_members:
        assert "id" in crew_members[0], "Crew object should have an 'id' field."
        assert "name" in crew_members[0], "Crew object should have a 'name' field."
        assert "agency" in crew_members[0], "Crew object should have an 'agency' field."
    print("✅ Crew details test passed!")
