from enum import Enum


class TemplateLocations(Enum):
    APPLICATION = 'src/main/java/application.tpl'
    POM = 'pom.tpl'
    ENTITY = 'src/main/java/entity/entity.tpl'

    def __str__(self):
        return str(self.value)
