import os
from jinja2 import Environment, FileSystemLoader

from app.generator.constants import APPLICATION_TEMPLATE, POM_TEMPLATE, PROPERTY_TEMPLATE, OUTPUT_LOCATION, \
    PATH_DELIMITER, JAVA_EXTENSION, TEMPLATES
from app.generator.utils.generatorutils import GeneratorUtil


def generate_layer(data, template, prefix, suffix):
    base_package = GeneratorUtil.get_base_package(data)
    base_data = GeneratorUtil.get_base_data(data)
    for entity_detail in data['entityDetails']:
        generate_component(base_data, entity_detail, base_package, template, prefix, suffix)


def generate_component(base_data, entity_data, base_package, template, prefix, suffix):
    coded_template = generate_template(template, entity_data, base_data)
    file = base_package + PATH_DELIMITER + prefix + PATH_DELIMITER + entity_data['entityName'] + suffix + JAVA_EXTENSION
    create_file(file, coded_template)


def generate_template(template_location, data, base_data):
    """"
    This function mainly used for generating the templates with metadata.
    @Input Metadata
    @Output Coded Template
    """
    file_loader = FileSystemLoader(TEMPLATES)
    environment = Environment(loader=file_loader)
    template = environment.get_template(template_location)
    return template.render(data=data, base=base_data)


def create_file(filename, content):
    filename = OUTPUT_LOCATION + filename
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as file:
        file.write(content)


def generate_application(data):
    coded_template = generate_template(APPLICATION_TEMPLATE, data, GeneratorUtil.get_base_data(data))
    file = GeneratorUtil.get_base_package(data) + data['name'] + "Application.java"
    create_file(file, coded_template)


def generate_pom(data):
    coded_template = generate_template(POM_TEMPLATE, data, GeneratorUtil.get_base_data(data))
    create_file(data['artifactId'] + '/pom.xml', coded_template)


def generate_properties(data):
    coded_template = generate_template(PROPERTY_TEMPLATE, data, GeneratorUtil.get_base_data(data))
    file = GeneratorUtil.get_resource_package(data) + "application.properties"
    create_file(file, coded_template)
