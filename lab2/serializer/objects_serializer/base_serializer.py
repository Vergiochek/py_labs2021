def object_to_dict(obj):
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