from my_p import MyParser
import json


class JsonParser(MyParser):
    def dump(self, save_file_path, obj):
        with open(save_file_path, 'w') as file:
            file.write(json.dumps(obj))

    def dumps(self, obj):
        return json.dumps(obj)

    def load(self, load_file_path):
        with open(load_file_path, 'r') as file:
            return json.loads(file.read())

    def loads(self, string_to_load):
        return json.loads(string_to_load)