import sys
import json
from jsonschema import exceptions, validate

JSON_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string", "minLength": 1},
        "course": {"type": "string", "minLength": 1, "enum": ["MS", "MSc"]},
        "subjects": {
            "type": "array",
            "minItems": 1
        },
        "email": {"type": "string", "minLength": 1},
        "thesis": {
            "type": "object",
            "properties": {
                "title": {"type": "string"}
            },
            "required": ["title"]
        }
    },
    "required": [
        "id",
        "name",
        "subjects",
        "email",
        "thesis"
    ]
}

with open("student.json") as file_obj:
    data = json.load(file_obj)

try:
    validate(instance=data, schema=JSON_SCHEMA)
except exceptions.ValidationError as validation_err:
    print("Failed {}".format(validation_err))
    sys.exit(1)

print("Pass")