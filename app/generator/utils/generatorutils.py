from app.generator.constants import APPLICATION_PACKAGE, RESOURCE_PACKAGE


class GeneratorUtil:

    @staticmethod
    def get_base_package(data):
        package = str(data['package']).replace(".", "/")
        return data['artifactId']+APPLICATION_PACKAGE+package+"/"

    @staticmethod
    def get_resource_package(data):
        return data['artifactId']+RESOURCE_PACKAGE

    @staticmethod
    def get_base_data(data):
        base_data = {"package":  data['package']}
        return base_data
