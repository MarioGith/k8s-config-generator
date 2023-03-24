from file_handle.file_handle import read_yaml, write_yaml
from generator.config_file import ConfigFile


class quota_generator(ConfigFile):
    def __init__(self, quota_name, namespace, template_file, output_file, request_cpu, request_memory, limit_cpu, limit_memory):
        super().__init__(quota_name, template_file, output_file)
        self.namespace = namespace
        self.request_cpu = request_cpu
        self.request_memory = request_memory
        self.limit_cpu = limit_cpu
        self.limit_memory = limit_memory

    def generate(self):
        data = read_yaml(self.template_file)
        data["metadata"]["name"] = self.config_name
        data["metadata"]["namespace"] = self.namespace
        data["spec"]["hard"]["requests.cpu"] = self.request_cpu
        data["spec"]["hard"]["requests.memory"] = self.request_memory
        data["spec"]["hard"]["limits.cpu"] = self.limit_cpu
        data["spec"]["hard"]["limits.memory"] = self.limit_memory
        write_yaml(self.output_file, data)
