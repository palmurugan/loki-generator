import json

from app.generator.coregenerator import CoreGenerator
from app.generator.dtogenerator import DTOGenerator
from app.generator.implgenerator import ImplGenerator
from app.generator.parentgenerator import ParentGenerator

with open('metadata/base_app.json', 'r') as metadata:
    application_metadata = json.load(metadata)

''' CoreGenerator().generate_persistence_layer(application_metadata) '''

ParentGenerator().generate_parent_project(application_metadata)

DTOGenerator().generate_dto_project(application_metadata)

CoreGenerator().generate_core_project(application_metadata)

ImplGenerator().generate_impl_project(application_metadata)
