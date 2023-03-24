from file_handle.file_handle import read_yaml, write_yaml
from generator.config_file import ConfigFile


class role_binding_generator(ConfigFile):
    def __init__(
        self,
        role_bindin_name,
        namespace,
        team_name,
        role_name,
        template_file,
        output_file,
    ):
        super().__init__(role_bindin_name, template_file, output_file)

        self.namespace = namespace
        self.team = team_name
        self.role = role_name

    def generate(self):
        data = read_yaml(self.template_file)
        data["metadata"]["name"] = self.config_name
        data["metadata"]["namespace"] = self.namespace
        data["subjects"][0]["name"] = self.team
        data["roleRef"]["name"] = self.role
        write_yaml(self.output_file, data)
