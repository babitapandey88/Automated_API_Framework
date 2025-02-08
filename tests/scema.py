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
