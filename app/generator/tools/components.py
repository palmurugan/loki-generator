from app.generator.constants import ENTITY_TEMPLATE, REPOSITORY_TEMPLATE, SERVICE_TEMPLATE, SERVICE_IMPL_TEMPLATE, \
    REST_RESOURCE_TEMPLATE
from app.generator.tools.builder import generate_application, generate_pom, generate_layer, generate_properties


def application_component(data):
    generate_application(data)
    return data


def pom_component(data):
    generate_pom(data)
    return data


def entity_component(data):
    generate_layer(data, 'core', ENTITY_TEMPLATE, 'entity', 'Entity')
    return data


def repository_component(data):
    generate_layer(data, 'core', REPOSITORY_TEMPLATE, 'repository', 'EntityRepository')
    return data


def service_component(data):
    generate_layer(data, 'core', SERVICE_TEMPLATE, 'service', 'Service')
    return data


def service_impl_component(data):
    generate_layer(data, 'core', SERVICE_IMPL_TEMPLATE, 'service/impl', 'ServiceImpl')
    return data


def resource_component(data):
    generate_layer(data, 'core', REST_RESOURCE_TEMPLATE, 'web/resource', 'Resource')
    return data


def property_component(data):
    generate_properties(data)
    return data
