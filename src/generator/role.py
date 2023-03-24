from file_handle.file_handle import read_yaml, write_yaml
from generator.config_file import ConfigFile


class role_generator(ConfigFile):
    def __init__(self, role_name, namespace, template_file, output_file, role_resources, verbs):
        super().__init__(role_name, template_file, output_file)
        self.namespace = namespace
        self.role_resources = role_resources
        self.verbs = verbs

    def generate(self):
        data = read_yaml(self.template_file)
        data["metadata"]["name"] = self.config_name
        data["metadata"]["namespace"] = self.namespace
        write_yaml(self.output_file, data)
