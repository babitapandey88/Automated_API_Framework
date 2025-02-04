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
