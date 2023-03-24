from file_handle.file_handle import read_yaml, write_yaml
from configparser import ConfigParser


class conf_generator(object):
    def __init__(self, team, output):
        self.team = team
        self.template = "../templates/config.cnf"
        self.output = output

    def generate(self):
        config_object = ConfigParser()
        config_object.optionxform = str
        config_object.read(self.template)
        config_object[" dn "]["CN"] = self.team
        with open(self.output, "w") as conf:
            config_object.write(conf)
