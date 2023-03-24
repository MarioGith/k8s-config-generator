import os
from file_handle.file_handle import read_yaml


class ConfigFile:
    def __init__(self, config_name, template_file, output_file):
        self.config_name = config_name
        self.template_file = template_file
        self.output_file = output_file

    def apply(self):
        os.system(f"kubectl apply -f {self.output_file}")
