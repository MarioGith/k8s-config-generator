from file_handle.file_handle import read_yaml, write_yaml
from generator.config_file import ConfigFile


class namespace_generator(ConfigFile):
    def __init__(self, team_name, template_file, output_file):
        super().__init__(team_name, template_file, output_file)

    def generate(self):
        data = read_yaml(self.template_file)
        data["metadata"]["name"] = self.config_name
        write_yaml(self.output_file, data)
