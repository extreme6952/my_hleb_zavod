import json
import django
from django.apps import apps
from django.db import models

def get_model_metadata():
    metadata = []
    for model in apps.get_models():
        model_info = {
            'name': model.__name__,
            'fields': []
        }
        for field in model._meta.get_fields():
            field_info = {
                'name': field.name,
                'type': field.__class__.__name__
            }
            model_info['fields'].append(field_info)
        metadata.append(model_info)
    return metadata

django.setup()

metadata = get_model_metadata()
print(json.dumps(metadata, indent=4))
