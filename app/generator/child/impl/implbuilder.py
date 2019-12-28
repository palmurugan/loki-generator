from app.generator.constants import IMPL_POM_TEMPLATE, IMPL_SWAGGER_CONFIG_TEMPLATE, \
    IMPL_SWAGGER_CONFIG_PROPERTIES_TEMPLATE
from app.generator.tools.builder import generate_template, create_file
from app.generator.utils import generatorutils
from app.generator.utils.generatorutils import GeneratorUtil


def generate_impl_pom(data):
    coded_template = generate_template(IMPL_POM_TEMPLATE, data, GeneratorUtil.get_base_data(data))
    create_file(data['artifactId'] + '/' + data['artifactId'] + '-impl' + '/pom.xml', coded_template)


def generate_impl_swagger_config(data):
    base_path = GeneratorUtil.get_base_package(data, 'impl')
    coded_template = generate_template(IMPL_SWAGGER_CONFIG_TEMPLATE, data, GeneratorUtil.get_base_data(data))
    create_file(base_path + 'impl/config/SwaggerConfig.java', coded_template)


def generate_impl_swagger_config_prop(data):
    base_path = GeneratorUtil.get_base_package(data, 'impl')
    coded_template = generate_template(IMPL_SWAGGER_CONFIG_PROPERTIES_TEMPLATE, data, GeneratorUtil.get_base_data(data))
    create_file(base_path + 'impl/config/SwaggerConfigProperties.java', coded_template)
