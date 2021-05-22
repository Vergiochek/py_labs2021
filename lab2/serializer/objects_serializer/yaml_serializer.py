import yaml
from serializer.objects_serializer.base_serializer import *


class YamlSerializer(ISerializer):
    def dumps(self, obj: object) -> str:
        return yaml.dump(object_to_dict(), sort_keys=False)

    def loads(self, s: str) -> object:
        return yaml.full_load(s)


class YamlFactory(SerializerFactory):
    def get_serializer(self) -> ISerializer:
        return YamlSerializer()
