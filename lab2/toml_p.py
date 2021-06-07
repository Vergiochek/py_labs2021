import toml
from my_p import MyParser


class TomlParser(MyParser):
    def dump(self, save_file_path, obj):
        with open(save_file_path, 'w') as file:
            toml.dump(obj, file)

    def dumps(self, obj):
        return toml.dumps(obj)

    def load(self, load_file_path):
        with open(load_file_path, 'r') as file:
            return toml.loads(file.read())

    def loads(self, toml_string):
        return toml.loads(toml_string)