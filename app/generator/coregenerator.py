from app.generator.tools import composer
from app.generator.tools.components import entity_component, repository_component, application_component, \
    property_component, pom_component


class CoreGenerator:

    def generate_persistence_layer(self, data):
        composer.compose(application_component(data), pom_component(data), entity_component(data),
                         repository_component(data), property_component(data))

