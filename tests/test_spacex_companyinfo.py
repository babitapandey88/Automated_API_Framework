import json
import os
import sys
import requests
import pytest
from jsonschema import validate
from config import BASE_URL
from tests.scema import company_info_schema
# Ensure config.py can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

def test_get_company_info():
    """Test to validate SpaceX company information API response."""
    url = f"{config.BASE_URL}/company"
    response = requests.get(url)
    assert response.status_code == 200, "Failed to fetch SpaceX company information."
    company_info = response.json()
    print(company_info)
    assert isinstance(company_info, dict), "Company info should be an object."
    validate(instance=company_info, schema=company_info_schema)
    print("✅ JSON Schema Validation Passed for Company Info!")