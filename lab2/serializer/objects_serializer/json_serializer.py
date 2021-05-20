import json
from serializer.objects_serializer.base_serializer import *


class JsonSerializer(ISerializer):
    def dumps(self, obj: object) -> str:
        return json.dumps(object_to_dict(obj), indent=4)

    def loads(self, s: str) -> object:
        return json.loads(s)


class JsonFactory(SerializerFactory):
    def get_serializer(self) -> ISerializer:
        return JsonSerializer()