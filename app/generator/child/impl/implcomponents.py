from app.generator.child.impl.implbuilder import generate_impl_pom
from app.generator.constants import IMPL_REPOSITORY_TEMPLATE, IMPL_SERVICE_TEMPLATE, IMPL_SERVICE_IMPL_TEMPLATE, \
    IMPL_REST_RESOURCE_TEMPLATE
from app.generator.tools.builder import generate_layer
IMPL_PROJECT = 'impl'


def impl_pom_component(data):
    generate_impl_pom(data)
    return data


def impl_repository_component(data):
    generate_layer(data, IMPL_REPOSITORY_TEMPLATE, 'impl/repository', 'EntityRepositoryExt', IMPL_PROJECT)
    return data


def impl_service_component(data):
    generate_layer(data, IMPL_SERVICE_TEMPLATE, 'impl/service', 'ServiceExt', IMPL_PROJECT)
    return data


def impl_service_impl_component(data):
    generate_layer(data, IMPL_SERVICE_IMPL_TEMPLATE, 'impl/service/impl', 'ServiceImplExt', IMPL_PROJECT)
    return data


def impl_resource_component(data):
    generate_layer(data, IMPL_REST_RESOURCE_TEMPLATE, 'impl/web/resource', 'ResourceExt', IMPL_PROJECT)
    return data
