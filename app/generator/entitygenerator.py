from app.generator.basegenerator import BaseGenerator
from app.generator.constants import ENTITY_TEMPLATE
from app.generator.utils.generatorutils import GeneratorUtil


class EntityGenerator(BaseGenerator):

    def generate(self, data):
        base_package = GeneratorUtil.get_base_package(data)
        for entity_detail in data['entityDetails']:
            self.__generate_entity(entity_detail, base_package)

    def __generate_entity(self, entity_detail, base_package):
        coded_template = super().generate_template(ENTITY_TEMPLATE, entity_detail)
        file = base_package+"/entity/"+entity_detail['entityName']+".java"
        super().create_file(file, coded_template)
