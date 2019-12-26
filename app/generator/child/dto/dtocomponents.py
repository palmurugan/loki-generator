from app.generator.child.dto.dtobuilder import generate_dto_pom


def dto_pom_component(data):
    generate_dto_pom(data)
    return data
