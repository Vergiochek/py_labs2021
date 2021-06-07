from toml_p import TomlParser
from yaml_p import YamlParser
from pickle_p import PickleParser
from json_p import JsonParser
import my_p

class Serializer:
    @staticmethod
    def serialize(obj, format):
        expr_type = make_choice(fst_prm="dump", sec_prm="dumps", th_prm="load", fth_prm="loads")
        serializer = get_serializer(format)
        if expr_type == "dump":
            file_path = get_file_path()
            serializer.dump(serializer, file_path, my_p.pack(obj))
        elif expr_type == "dumps":
            loaded_string = serializer.dumps(serializer, my_p.pack(obj))
            print(loaded_string)
        elif expr_type == "load":
            file_path = get_file_path()
            loaded_obj = my_p.unpack(serializer.load(serializer, file_path))
            print(loaded_obj)
        elif expr_type == "loads":
            obj_string = get_obj_string()
            loaded_obj = my_p.unpack(serializer.loads(serializer, obj_string))
            print(loaded_obj)


def get_serializer(format):
    if format == 'JSON':
        return JsonParser
    elif format == 'PICKLE':
        return PickleParser
    elif format == 'TOML':
        return TomlParser
    elif format == 'YAML':
        return YamlParser
    else:
        raise ValueError(format)


def get_file_path():
    print("input file path: ")
    user_input = str(input())
    return user_input


def get_obj_string():
    print("input object string representation: ")
    user_input = str(input())
    return user_input


def make_choice(fst_prm, sec_prm, th_prm, fth_prm):
    print(f"1 - {fst_prm}\n"
          f"2 - {sec_prm}\n"
          f"3 - {th_prm}\n"
          f"4 - {fth_prm}\n"
          "5 - quit")
    user_input = int(input())
    if user_input == 1:
        return fst_prm
    elif user_input == 2:
        return sec_prm
    elif user_input == 3:
        return th_prm
    elif user_input == 4:
        return fth_prm
    else:
        exit(0)