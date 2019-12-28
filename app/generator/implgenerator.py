from app.generator.child.impl.implbuilder import generate_impl_pom
from app.generator.child.impl.implcomponents import impl_repository_component, impl_service_component, \
    impl_service_impl_component, impl_resource_component, impl_swagger_config_component, \
    impl_swagger_config_prop_component
from app.generator.tools import composer


class ImplGenerator:
    def generate_impl_project(self, data):
        composer.compose(generate_impl_pom(data), impl_repository_component(data), impl_service_component(data),
                         impl_service_impl_component(data), impl_resource_component(data),
                         impl_swagger_config_component(data), impl_swagger_config_prop_component(data))
