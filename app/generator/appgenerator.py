from app.generator.constants import APPLICATION_TEMPLATE
from app.generator.basegenerator import BaseGenerator
from app.generator.utils.generatorutils import GeneratorUtil


class AppGenerator(BaseGenerator):

    def generate(self, data):
        coded_template = super().generate_template(APPLICATION_TEMPLATE, data)
        file = GeneratorUtil.get_base_package(data) + data['name'] + "Application.java"
        super().create_file(file, coded_template)
