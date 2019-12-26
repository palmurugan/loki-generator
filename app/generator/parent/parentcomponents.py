from app.generator.parent.parentbuilder import generate_parent_pom


def parent_pom_component(data):
    generate_parent_pom(data)
    return data
