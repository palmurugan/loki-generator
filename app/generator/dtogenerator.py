from app.generator.child.dto.dtocomponents import dto_pom_component, dto_component
from app.generator.tools import composer


class DTOGenerator:
    def generate_dto_project(self, data):
        composer.compose(dto_pom_component(data), dto_component(data))
