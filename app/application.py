import json
from app.generator.pomgenerator import POMGenerator
from app.generator.appgenerator import AppGenerator
from app.generator.entitygenerator import EntityGenerator

with open('metadata/base_app.json', 'r') as metadata:
    application_dict = json.load(metadata)

AppGenerator().generate(application_dict)
POMGenerator().generate(application_dict)
EntityGenerator().generate(application_dict)
