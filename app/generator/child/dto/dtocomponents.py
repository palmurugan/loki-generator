from app.generator.child.dto.dtobuilder import generate_dto_pom
from app.generator.constants import DTO_TEMPLATE
from app.generator.tools.builder import generate_layer


def dto_pom_component(data):
    generate_dto_pom(data)
    return data


def dto_component(data):
    generate_layer(data, DTO_TEMPLATE, 'dto', 'DTO', 'dto')
    return data
