import toml
from serializer.objects_serializer.base_serializer import *


class TomlSerializer(ISerializer):
    def dumps(self, obj: object) -> str:
        return toml.dumps(obj)

    def loads(self, s: str) -> object:
        return toml.loads(s)


class TomlFactory(SerializerFactory):
    def get_serializer(self) -> ISerializer:
        return TomlSerializer()
