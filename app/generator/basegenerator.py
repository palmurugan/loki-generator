import os
from abc import ABC
from jinja2 import Environment, FileSystemLoader


class BaseGenerator(ABC):

    BASE_LOCATION = '/Users/palmurugan/tmp/'

    def generate_template(self, template_location,  data):
        file_loader = FileSystemLoader('templates')
        environment = Environment(loader=file_loader)
        template = environment.get_template(template_location)
        return template.render(data=data)

    def create_file(self, filename, content):
        filename = self.BASE_LOCATION+filename
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, 'w') as file:
            file.write(content)

