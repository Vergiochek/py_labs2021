import pickle
from serializer.objects_serializer.base_serializer import *


class PickleSerializer(ISerializer):
    def dumps(self, obj: object) -> str:
        return str(pickle.dumps(obj))

    def loads(self, s: str) -> object:
        return pickle.loads(bytes(s))


class PickleFactory(SerializerFactory):
    def get_serializer(self) -> ISerializer:
        return PickleSerializer()

    def loads(self, s: str, cls=None) -> object:
        serial = self.get_serializer()
        return serial.loads(s)

    def dump(self, obj, path):
        s = self.dumps(obj)
        f = open(path, 'wb')
        f.write(bytes(s))
        f.close()

    def load(self, path: str, cls=None) -> object:
        f = open(path, 'rb')
        s = f.read()
        f.close()
        return self.loads(str(s), cls)