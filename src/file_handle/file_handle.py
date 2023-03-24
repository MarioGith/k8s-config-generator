import os
import yaml

def read_yaml(config_path):
    """A function to read YAML file"""
    with open(config_path) as f:
        config = yaml.safe_load(f)
    return config


def write_yaml(save_path, data):
    """A function to write YAML file"""
    with open(save_path, "w") as f:
        yaml.dump(data, f)


def write_file(save_path, data):
    """A function to write simple file"""
    with open(save_path, "w") as f:
        f.write(data)
    f.close()
