from app.generator.constants import APPLICATION_PACKAGE


class GeneratorUtil:

    @staticmethod
    def get_base_package(data):
        package = str(data['package']).replace(".", "/")
        return data['artifactId']+APPLICATION_PACKAGE+package+"/"

