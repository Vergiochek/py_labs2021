import yaml
from my_p import MyParser


class YamlParser(MyParser):
    def dump(self, save_file_path, obj):
        with open(save_file_path, 'w') as file:
            yaml.dump(obj, file, default_flow_style=False)

    def dumps(self, obj):
        return yaml.dump(obj)

    def load(self, load_file_path):
        with open(load_file_path, 'r') as file:
            return yaml.unsafe_load(file.read())

    def loads(self, data):
        return yaml.unsafe_load(data)