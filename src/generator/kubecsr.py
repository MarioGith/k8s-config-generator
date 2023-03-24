from file_handle.file_handle import read_yaml, write_yaml


class kubecsr_generator(object):
    def __init__(self, name, output):
        self.name = name
        self.template = "../templates/kubecsr.yaml"
        self.output = output

    def generate(self):
        data = read_yaml(self.template)
        data["metadata"]["name"] = self.name
        write_yaml(self.output, data)
