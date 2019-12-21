import json

from app.generator.coregenerator import CoreGenerator

with open('metadata/base_app.json', 'r') as metadata:
    application_metadata = json.load(metadata)

CoreGenerator().generate_persistence_layer(application_metadata)
