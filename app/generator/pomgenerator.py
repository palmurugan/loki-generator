from app.generator.constants import POM_TEMPLATE
from app.generator.basegenerator import BaseGenerator


class POMGenerator(BaseGenerator):

    def generate(self, data):
        coded_template = super().generate_template(POM_TEMPLATE,  data)
        super().create_file(data['artifactId'] + '/pom.xml', coded_template)
