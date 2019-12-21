from app.generator.constants import ENTITY_TEMPLATE, REPOSITORY_TEMPLATE
from app.generator.tools.builder import generate_application, generate_pom, generate_layer, generate_properties


def application_component(data):
    generate_application(data)
    return data


def pom_component(data):
    generate_pom(data)
    return data


def entity_component(data):
    generate_layer(data, ENTITY_TEMPLATE, 'entity', 'Entity')
    return data


def repository_component(data):
    generate_layer(data, REPOSITORY_TEMPLATE, 'repository', 'EntityRepository')
    return data


def property_component(data):
    generate_properties(data)
    return data
