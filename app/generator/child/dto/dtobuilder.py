from app.generator.constants import PARENT_POM_TEMPLATE, DTO_POM_TEMPLATE
from app.generator.tools.builder import generate_template, create_file
from app.generator.utils.generatorutils import GeneratorUtil


def generate_dto_pom(data):
    coded_template = generate_template(DTO_POM_TEMPLATE, data, GeneratorUtil.get_base_data(data))
    create_file(data['artifactId'] + '/' + data['artifactId'] + '-dto' + '/pom.xml', coded_template)

