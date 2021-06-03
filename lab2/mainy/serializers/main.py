import sys, os
sys.path.insert(0, '/mainy/serializers')
from serializers import *


def choose(ext):
    if ext == '.json':
        return SerializerFactory.get_instance(SerializerType.Json)
    elif ext == '.yaml':
        return SerializerFactory.get_instance(SerializerType.Yaml)
    elif ext == '.pickle':
        return SerializerFactory.get_instance(SerializerType.Pickle)
    elif ext == '.toml':
        return SerializerFactory.get_instance(SerializerType.Toml)


def get_ext(path):
    return os.path.splitext(path)[1]


def main():
    config_reader = SerializerFactory.get_instance(SerializerType.Json)
    config = config_reader.load('/home/Daniil/Desktop/py_labs2021/lab2/mainy/serializers/config.json')

    source_serializer = choose(get_ext(config.path))
    obj = source_serializer.load(config.path)
    target_serializer = choose(get_ext(config.target_file))
    target_serializer.dump(obj, config.target_file)


if __name__ == '__main__':
    main()
