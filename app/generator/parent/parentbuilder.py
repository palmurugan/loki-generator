from app.generator.constants import PARENT_POM_TEMPLATE
from app.generator.tools.builder import generate_template, create_file
from app.generator.utils.generatorutils import GeneratorUtil


def generate_parent_pom(data):
    coded_template = generate_template(PARENT_POM_TEMPLATE, data, GeneratorUtil.get_base_data(data))
    create_file(data['artifactId'] + '/pom.xml', coded_template)

