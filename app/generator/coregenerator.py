from app.generator.child.core.corebuilder import generate_core_pom
from app.generator.child.core.corecomponents import core_entity_component, core_repository_component, \
    core_service_component, core_service_impl_component, core_resource_component, core_mapper_component
from app.generator.tools import composer
from app.generator.tools.components import entity_component, repository_component, application_component, \
    property_component, pom_component, service_component, service_impl_component, resource_component


class CoreGenerator:

    def generate_persistence_layer(self, data):
        composer.compose(application_component(data), pom_component(data), entity_component(data),
                         repository_component(data), service_component(data), service_impl_component(data),
                         resource_component(data), property_component(data))

    def generate_core_project(self, data):
        composer.compose(generate_core_pom(data), core_entity_component(data),
                         core_repository_component(data), core_service_component(data),
                         core_service_impl_component(data), core_resource_component(data), core_mapper_component(data))
