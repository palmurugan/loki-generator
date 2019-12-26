from app.generator.parent.parentcomponents import parent_pom_component
from app.generator.tools import composer


class ParentGenerator:
    def generate_parent_project(self, data):
        composer.compose(parent_pom_component(data))
