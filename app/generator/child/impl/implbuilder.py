from app.generator.constants import IMPL_POM_TEMPLATE
from app.generator.tools.builder import generate_template, create_file
from app.generator.utils.generatorutils import GeneratorUtil


def generate_impl_pom(data):
    coded_template = generate_template(IMPL_POM_TEMPLATE, data, GeneratorUtil.get_base_data(data))
    create_file(data['artifactId'] + '/' + data['artifactId'] + '-impl' + '/pom.xml', coded_template)

