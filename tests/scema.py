#schemas define the expected structure of JSON responses from the SpaceX API
launch_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "date_utc": {"type": "string"},
        "success": {"type": ["boolean", "null"]},  # Can be True, False, or Null
        "rocket": {"type": "string"}
    },
    "required": ["id", "name", "date_utc", "rocket"]  # Fields that must exist
}

rocket_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "active": {"type": "boolean"}
        },
        "required": ["id", "name", "active"]
    }
}

roadster_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "launch_date_utc": {"type": "string", "format": "date-time"},
        "earth_distance_km": {"type": "number"},
        "mars_distance_km": {"type": "number"}
    },
    "required": ["id", "name", "launch_date_utc", "earth_distance_km", "mars_distance_km"]
}
company_info_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "founder": {"type": "string"},
        "founded": {"type": "integer"},
        "employees": {"type": "integer"},
        "vehicles": {"type": "integer"},
        "launch_sites": {"type": "integer"},
        "test_sites": {"type": "integer"},
        "ceo": {"type": "string"},
        "cto": {"type": "string"},
        "valuation": {"type": "number"},
        "summary": {"type": "string"}
    },
    "required": ["name", "founder", "founded", "employees", "ceo", "valuation"]
}
