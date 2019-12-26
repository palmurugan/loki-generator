from app.generator.constants import APPLICATION_PACKAGE, RESOURCE_PACKAGE, PATH_DELIMITER


class GeneratorUtil:

    @staticmethod
    def get_base_package(data, build_type=None):
        package = str(data['package']).replace(".", PATH_DELIMITER)
        if build_type is not None:
            path = data['artifactId'] + PATH_DELIMITER + data[
                'artifactId'] + '-' + build_type + APPLICATION_PACKAGE + package + PATH_DELIMITER
        else:
            path = data['artifactId'] + APPLICATION_PACKAGE + package + PATH_DELIMITER
        return path

    @staticmethod
    def get_resource_package(data):
        return data['artifactId'] + RESOURCE_PACKAGE

    @staticmethod
    def get_base_data(data):
        base_data = {"package": data['package']}
        return base_data
