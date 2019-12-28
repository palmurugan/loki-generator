from app.generator.child.core.corebuilder import generate_core_pom
from app.generator.constants import ENTITY_TEMPLATE, REPOSITORY_TEMPLATE, SERVICE_TEMPLATE, SERVICE_IMPL_TEMPLATE, \
    REST_RESOURCE_TEMPLATE, MAPPER_TEMPLATE
from app.generator.tools.builder import generate_layer

CORE_PROJECT = 'core'


def core_pom_component(data):
    generate_core_pom(data)
    return data


def core_entity_component(data):
    generate_layer(data, ENTITY_TEMPLATE, 'core/entity', 'Entity', CORE_PROJECT)
    return data


def core_repository_component(data):
    generate_layer(data, REPOSITORY_TEMPLATE, 'core/repository', 'EntityRepository', CORE_PROJECT)
    return data


def core_service_component(data):
    generate_layer(data, SERVICE_TEMPLATE, 'core/service', 'Service', CORE_PROJECT)
    return data


def core_service_impl_component(data):
    generate_layer(data, SERVICE_IMPL_TEMPLATE, 'core/service/impl', 'ServiceImpl', CORE_PROJECT)
    return data


def core_resource_component(data):
    generate_layer(data, REST_RESOURCE_TEMPLATE, 'core/web/resource', 'Resource', CORE_PROJECT)
    return data


def core_mapper_component(data):
    generate_layer(data, MAPPER_TEMPLATE, 'core/mapper', 'Mapper', CORE_PROJECT)
    return data
