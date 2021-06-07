from abc import abstractmethod
from types import CodeType, FunctionType
import dill
import inspect
import builtins
from data import Car


def is_primitive(obj):
    return type(obj) in [int, float, str, bool, type(None), list, tuple]


def function_to_dictionary(obj):
    members = inspect.getmembers(obj.__code__)
    func_dict = {}
    for item in members:
        if item[0].startswith('co_'):
            func_dict[item[0]] = item[1]
    func_dict['co_code'] = list(func_dict["co_code"])
    func_dict['co_lnotab'] = list(func_dict["co_lnotab"])
    func = {'code': func_dict}
    function_globals = dict()
    name = func['code']['co_name']
    function_globals[name] = name + '<function>'
    global_pairs = obj.__globals__.items()
    for (key, value) in global_pairs:
        if is_primitive(value):
            function_globals[key] = value
    func['globals'] = function_globals
    return func


def convert_to_function(dict_func):
    function_globals = dict_func['globals']
    function_globals['__builtins__'] = builtins
    code_args = dict_func['code']
    my_obj = CodeType(code_args['co_argcount'],
                   code_args['co_posonlyargcount'],
                   code_args['co_kwonlyargcount'],
                   code_args['co_nlocals'],
                   code_args['co_stacksize'],
                   code_args['co_flags'],
                   bytes(code_args['co_code']),
                   tuple(code_args['co_consts']),
                   tuple(code_args['co_names']),
                   tuple(code_args['co_varnames']),
                   code_args['co_filename'],
                   code_args['co_name'],
                   code_args['co_firstlineno'],
                   bytes(code_args['co_lnotab']),
                   tuple(code_args['co_freevars']),
                   tuple(code_args['co_cellvars']))
    temp = FunctionType(my_obj, function_globals, code_args['co_name'])
    name = code_args['co_name']
    function_globals[name] = temp
    return FunctionType(my_obj, function_globals, name)


def object_to_dictionary(obj):
    struct = {'__type__': 'object', '__class__': obj.__class__.__name__}
    for attr in dir(obj):
        if not attr.startswith('__'):
            attr_value = getattr(obj, attr)
            if callable(attr_value):
                if len(attr_value.__code__.co_varnames) > 1:
                    struct[attr] = function_to_dictionary(attr_value)
            elif "<class '__main__." in str(attr_value.__class__):
                struct[attr] = object_to_dictionary(attr_value)
            else:
                struct[attr] = attr_value
    return struct


def class_to_dictionary(cl):
    if cl.__class__.__name__ == "type":
        struct = {'__type__': 'class', '__class__': cl.__name__}
        for attr in dir(cl):
            if attr == "__init__":
                attr_value = getattr(cl, attr)
                struct[attr] = function_to_dictionary(attr_value)
            if not attr.startswith('__'):
                attr_value = getattr(cl, attr)
                if "<class 'type'>" in str(attr_value.__class__):
                    struct[attr] = class_to_dictionary(attr_value)
                elif "<class '__main__." in str(attr_value.__class__):
                    struct[attr] = object_to_dictionary(attr_value)
                elif callable(attr_value):
                    if len(inspect.getfullargspec(attr_value).args) > 1:
                        struct[attr] = function_to_dictionary(attr_value)
                    else:
                        struct[attr] = attr_value
        return struct


def convert_to_object(json_str):
    class_name = globals()[json_str['__class__']]
    init_args = inspect.getfullargspec(class_name).args
    args = {}
    for arg in init_args:
        if arg in json_str:
            args[arg] = json_str[arg]
    obj = class_name(**args)
    for attr in obj.__dir__():
        if isinstance(getattr(obj, attr), dict) and not attr.startswith('__'):
            object_attr = convert_to_object(getattr(obj, attr))
            setattr(obj, attr, object_attr)
        elif not attr.startswith('__') and attr not in args:
            object_attr = getattr(obj, attr)
            if not callable(object_attr):
                setattr(obj, attr, json_str[attr])
    return obj


def convert_to_class(json_str):
    vars = {}
    argsN = []
    print(json_str)

    def attr_init(self, *args):
        if len(args) > len(argsN):
            raise Exception("To much arguments!")
        ind = 0
        for argument in args:
            setattr(self, argsN[ind], argument)
            ind += 1

    for attr in json_str:
        if attr == '__init__':
            for arg in json_str[attr]['code']['co_varnames']:
                if arg != 'self':
                    argsN.append(arg)
            vars[attr] = attr_init
        elif not isinstance(json_str[attr], dict) and not attr.startswith('__'):
            vars[attr] = json_str[attr]
        elif isinstance(json_str[attr], dict) and not attr.startswith('__'):
            if json_str[attr]['__type__'] == 'function':
                vars[attr] = convert_to_function(json_str[attr])
    return type("method", (object,), vars)


def pack(obj):
    if isinstance(obj, FunctionType):
        obj_dict = function_to_dictionary(obj)
        return obj_dict
    elif is_primitive(obj):
        return obj
    elif isinstance(obj, type):
        obj_dict = class_to_dictionary(obj)
        return obj_dict
    elif isinstance(obj, object):
        obj_dict = object_to_dictionary(obj)
        return obj_dict


def unpack(load_dict):
    if "code" in load_dict.keys():
        return convert_to_function(load_dict)
    elif "object" in load_dict.values():
        return convert_to_object(load_dict)
    elif "class" in load_dict.values():
        return convert_to_class(load_dict)
    else:
        return load_dict


class MyParser:
    @abstractmethod
    def dump(self, file_path, obj):
        pass

    @abstractmethod
    def dumps(self, obj):
        pass

    @abstractmethod
    def load(self, file_path):
        pass

    @abstractmethod
    def loads(self, string):
        pass
