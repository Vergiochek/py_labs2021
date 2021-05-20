def object_to_dict(obj: object):
    if not hasattr(obj, '__dict__'):
        return obj
    else:
        dct = {}
        for elem in vars(obj):
            dct[elem] = object_to_dict(getattr(obj, elem))
        return dct


def dict_to_object(dct, cls):
    obj = cls()
    for elem in dict:
        setattr(obj, elem, dict[elem])
    return obj


class ISerializer:
    def dumps(self, obj: object) -> str:
        pass

    def loads(self, s: str) -> object:
        pass


class SerializerFactory:
    def get_serializer(self) -> ISerializer:
        pass

    def dumps(self, obj: object) -> str:
        serial = self.get_serializer()
        return serial.dumps(obj)

    def loads(self, s: str, cls=None) -> object:
        serial = self.get_serializer()
        dct = serial.loads(s)
        if cls is not None:
            return dict_to_object(dct, cls)
        else:
            return dct

    def dump(self, obj: object, path):
        s = self.dumps(obj)
        f = open(path, 'w')
        f.write(s)
        f.close()

    def load(self, path: str, cls=None) -> object:
        f = open(path, 'r')
        s = f.read()
        f.close()
        return self.loads(s, cls)