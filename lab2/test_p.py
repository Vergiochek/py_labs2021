import unittest
from data import Car, division, add_one
from toml_p import TomlParser
from yaml_p import YamlParser
from pickle_p import PickleParser
from json_p import JsonParser
import my_p


class TestParsers(unittest.TestCase):
    def setUp(self):
        self.Car = Car
        self.division = division
        self.lamb = add_one
        self.car = Car("Peugeot", "406")
        self.yaml_parser = YamlParser
        self.toml_parser = TomlParser
        self.json_parser = JsonParser
        self.pickle_parser = PickleParser

    # Test self class dump load
    def test_json_cl_dump_load(self):
        self.json_parser.dump(self.json_parser, './Tests/cl.json', my_p.pack(self.Car))
        obj_to_compare = my_p.unpack(self.json_parser.load(self.json_parser, './Tests/cl.json'))
        self.assertEqual(obj_to_compare.__class__, Car.__class__)

    def test_pickle_cl_dump_load(self):
        self.pickle_parser.dump(self.pickle_parser, './Tests/cl.pickle', my_p.pack(self.Car))
        obj_to_compare = my_p.unpack(self.pickle_parser.load(self.pickle_parser, './Tests/cl.pickle'))
        self.assertEqual(obj_to_compare.__class__, Car.__class__)

    def test_toml_cl_dump_load(self):
        self.toml_parser.dump(self.toml_parser, './Tests/cl.toml', my_p.pack(self.Car))
        obj_to_compare = my_p.unpack(self.toml_parser.load(self.toml_parser, './Tests/cl.toml'))
        self.assertEqual(obj_to_compare.__class__, Car.__class__)

    def test_yaml_cl_dump_load(self):
        self.yaml_parser.dump(self.yaml_parser, './Tests/cl.yml', my_p.pack(self.Car))
        obj_to_compare = my_p.unpack(self.yaml_parser.load(self.yaml_parser, './Tests/cl.yml'))
        self.assertEqual(obj_to_compare.__class__, Car.__class__)

    # Test self object dump load
    def test_json_obj_dump_load(self):
        self.json_parser.dump(self.json_parser, './Tests/obj.json', my_p.pack(self.car))
        obj_to_compare = my_p.unpack(self.json_parser.load(self.json_parser, './Tests/obj.json'))
        self.assertEqual(obj_to_compare.brand, self.car.brand)

    def test_pickle_obj_dump_load(self):
        self.pickle_parser.dump(self.pickle_parser, './Tests/obj.pickle', my_p.pack(self.car))
        obj_to_compare = my_p.unpack(self.pickle_parser.load(self.pickle_parser, './Tests/obj.pickle'))
        self.assertEqual(obj_to_compare.brand, self.car.brand)

    def test_toml_obj_dump_load(self):
        self.toml_parser.dump(self.toml_parser, './Tests/obj.toml', my_p.pack(self.car))
        obj_to_compare = my_p.unpack(self.toml_parser.load(self.toml_parser, './Tests/obj.toml'))
        self.assertEqual(obj_to_compare.brand, self.car.brand)

    def test_yaml_obj_dump_load(self):
        self.yaml_parser.dump(self.yaml_parser, './Tests/obj.yml', my_p.pack(self.car))
        obj_to_compare = my_p.unpack(self.yaml_parser.load(self.yaml_parser, './Tests/obj.yml'))
        self.assertEqual(obj_to_compare.brand, self.car.brand)

    # Test self func dump load
    def test_json_func_dump_load(self):
        self.json_parser.dump(self.json_parser, './Tests/func.json', my_p.pack(self.division))
        obj_to_compare = my_p.unpack(self.json_parser.load(self.json_parser, './Tests/func.json'))
        self.assertEqual(obj_to_compare(10, 2), 5)

    def test_pickle_func_dump_load(self):
        self.pickle_parser.dump(self.pickle_parser, './Tests/func.pickle', my_p.pack(self.division))
        obj_to_compare = my_p.unpack(self.pickle_parser.load(self.pickle_parser, './Tests/func.pickle'))
        self.assertEqual(obj_to_compare(10, 2), 5)

    def test_toml_func_dump_load(self):
        self.toml_parser.dump(self.toml_parser, './Tests/func.toml', my_p.pack(self.division))
        obj_to_compare = my_p.unpack(self.toml_parser.load(self.toml_parser, './Tests/func.toml'))
        self.assertEqual(obj_to_compare(10, 2), 5)

    def test_yaml_func_dump_load(self):
        self.yaml_parser.dump(self.yaml_parser, './Tests/func.yml', my_p.pack(self.division))
        obj_to_compare = my_p.unpack(self.yaml_parser.load(self.yaml_parser, './Tests/func.yml'))
        self.assertEqual(obj_to_compare(10, 2), 5)

    # Test self lambda dump load
    def test_json_lambda_dump_load(self):
        self.json_parser.dump(self.json_parser, './Tests/lamb.json', my_p.pack(self.lamb))
        obj_to_compare = my_p.unpack(self.json_parser.load(self.json_parser, './Tests/lamb.json'))
        self.assertEqual(obj_to_compare(2), 3)

    def test_pickle_lambda_dump_load(self):
        self.pickle_parser.dump(self.pickle_parser, './Tests/lamb.pickle', my_p.pack(self.lamb))
        obj_to_compare = my_p.unpack(self.pickle_parser.load(self.pickle_parser, './Tests/lamb.pickle'))
        self.assertEqual(obj_to_compare(2), 3)

    def test_yaml_lambda_dump_load(self):
        self.yaml_parser.dump(self.yaml_parser, './Tests/lamb.yml', my_p.pack(self.lamb))
        obj_to_compare = my_p.unpack(self.yaml_parser.load(self.yaml_parser, './Tests/lamb.yml'))
        self.assertEqual(obj_to_compare(2), 3)

    # Equal between other (objects)
    def test_pickle_json_obj_dump_load(self):
        self.json_parser.dump(self.json_parser, './Tests/obj.json', my_p.pack(self.car))
        from_json_to_compare = my_p.unpack(self.json_parser.load(self.json_parser, './Tests/obj.json'))
        self.pickle_parser.dump(self.pickle_parser, './Tests/obj.pickle', my_p.pack(self.car))
        from_pickle_to_compare = my_p.unpack(self.pickle_parser.load(self.pickle_parser, './Tests/obj.pickle'))
        self.assertEqual(from_json_to_compare.brand, from_pickle_to_compare.brand)

    def test_json_yaml_obj_dump_load(self):
        self.json_parser.dump(self.json_parser, './Tests/obj.json', my_p.pack(self.car))
        from_json_to_compare = my_p.unpack(self.json_parser.load(self.json_parser, './Tests/obj.json'))
        self.yaml_parser.dump(self.yaml_parser, './Tests/obj.yml', my_p.pack(self.car))
        from_yaml_to_compare = my_p.unpack(self.yaml_parser.load(self.yaml_parser, './Tests/obj.yml'))
        self.assertEqual(from_json_to_compare.brand, from_yaml_to_compare.brand)

    def test_toml_yaml_obj_dump_load(self):
        self.yaml_parser.dump(self.yaml_parser, './Tests/obj.yml', my_p.pack(self.car))
        from_yaml_to_compare = my_p.unpack(self.yaml_parser.load(self.yaml_parser, './Tests/obj.yml'))
        self.toml_parser.dump(self.toml_parser, './Tests/obj.toml', my_p.pack(self.car))
        from_toml_to_compare = my_p.unpack(self.toml_parser.load(self.toml_parser, './Tests/obj.toml'))
        self.assertEqual(from_yaml_to_compare.brand, from_toml_to_compare.brand)

    def test_yaml_pickle_obj_dump_load(self):
        self.pickle_parser.dump(self.pickle_parser, './Tests/obj.pickle', my_p.pack(self.car))
        from_pickle_to_compare = my_p.unpack(self.pickle_parser.load(self.pickle_parser, './Tests/obj.pickle'))
        self.yaml_parser.dump(self.yaml_parser, './Tests/obj.yml', my_p.pack(self.car))
        from_yaml_to_compare = my_p.unpack(self.yaml_parser.load(self.yaml_parser, './Tests/obj.yml'))
        self.assertEqual(from_pickle_to_compare.brand, from_yaml_to_compare.brand)

    # Equal between other (classes)
    def test_pickle_json_cl_dump_load(self):
        self.json_parser.dump(self.json_parser, './Tests/cl.json', my_p.pack(self.Car))
        from_json_to_compare = my_p.unpack(self.json_parser.load(self.json_parser, './Tests/cl.json'))
        self.pickle_parser.dump(self.pickle_parser, './Tests/cl.pickle', my_p.pack(self.Car))
        from_pickle_to_compare = my_p.unpack(self.pickle_parser.load(self.pickle_parser, './Tests/cl.pickle'))
        self.assertEqual(from_json_to_compare.__name__, from_pickle_to_compare.__name__)

    def test_json_yaml_cl_dump_load(self):
        self.json_parser.dump(self.json_parser, './Tests/cl.json', my_p.pack(self.Car))
        from_json_to_compare = my_p.unpack(self.json_parser.load(self.json_parser, './Tests/cl.json'))
        self.yaml_parser.dump(self.yaml_parser, './Tests/cl.yml', my_p.pack(self.Car))
        from_yaml_to_compare = my_p.unpack(self.yaml_parser.load(self.yaml_parser, './Tests/cl.yml'))
        self.assertEqual(from_json_to_compare.__name__, from_yaml_to_compare.__name__)

    def test_toml_yaml_cl_dump_load(self):
        self.yaml_parser.dump(self.yaml_parser, './Tests/cl.yml', my_p.pack(self.Car))
        from_yaml_to_compare = my_p.unpack(self.yaml_parser.load(self.yaml_parser, './Tests/cl.yml'))
        self.toml_parser.dump(self.toml_parser, './Tests/cl.toml', my_p.pack(self.Car))
        from_toml_to_compare = my_p.unpack(self.toml_parser.load(self.toml_parser, './Tests/cl.toml'))
        self.assertEqual(from_yaml_to_compare.__name__, from_toml_to_compare.__name__)

    def test_yaml_pickle_cl_dump_load(self):
        self.pickle_parser.dump(self.pickle_parser, './Tests/cl.pickle', my_p.pack(self.Car))
        from_pickle_to_compare = my_p.unpack(self.pickle_parser.load(self.pickle_parser, './Tests/cl.pickle'))
        self.yaml_parser.dump(self.yaml_parser, './Tests/cl.yml', my_p.pack(self.Car))
        from_yaml_to_compare = my_p.unpack(self.yaml_parser.load(self.yaml_parser, './Tests/cl.yml'))
        self.assertEqual(from_pickle_to_compare.__name__, from_yaml_to_compare.__name__)

    # Equal between other (functions)
    def test_pickle_json_func_dump_load(self):
        self.json_parser.dump(self.json_parser, './Tests/func.json', my_p.pack(self.division))
        from_json_to_compare = my_p.unpack(self.json_parser.load(self.json_parser, './Tests/func.json'))
        self.pickle_parser.dump(self.pickle_parser, './Tests/func.pickle', my_p.pack(self.division))
        from_pickle_to_compare = my_p.unpack(self.pickle_parser.load(self.pickle_parser, './Tests/func.pickle'))
        self.assertEqual(from_json_to_compare(10, 2), from_pickle_to_compare(10, 2))

    def test_json_yaml_func_dump_load(self):
        self.json_parser.dump(self.json_parser, './Tests/func.json', my_p.pack(self.division))
        from_json_to_compare = my_p.unpack(self.json_parser.load(self.json_parser, './Tests/func.json'))
        self.yaml_parser.dump(self.yaml_parser, './Tests/func.yml', my_p.pack(self.division))
        from_yaml_to_compare = my_p.unpack(self.yaml_parser.load(self.yaml_parser, './Tests/func.yml'))
        self.assertEqual(from_json_to_compare(10, 2), from_yaml_to_compare(10, 2))

    def test_toml_yaml_func_dump_load(self):
        self.yaml_parser.dump(self.yaml_parser, './Tests/func.yml', my_p.pack(self.division))
        from_yaml_to_compare = my_p.unpack(self.yaml_parser.load(self.yaml_parser, './Tests/func.yml'))
        self.toml_parser.dump(self.toml_parser, './Tests/func.toml', my_p.pack(self.division))
        from_toml_to_compare = my_p.unpack(self.toml_parser.load(self.toml_parser, './Tests/func.toml'))
        self.assertEqual(from_yaml_to_compare(10, 2), from_toml_to_compare(10, 2))

    def test_yaml_pickle_func_dump_load(self):
        self.pickle_parser.dump(self.pickle_parser, './Tests/func.pickle', my_p.pack(self.division))
        from_pickle_to_compare = my_p.unpack(self.pickle_parser.load(self.pickle_parser, './Tests/func.pickle'))
        self.yaml_parser.dump(self.yaml_parser, './Tests/func.yml', my_p.pack(self.division))
        from_yaml_to_compare = my_p.unpack(self.yaml_parser.load(self.yaml_parser, './Tests/func.yml'))
        self.assertEqual(from_pickle_to_compare(10, 2), from_yaml_to_compare(10, 2))

    # Equal between other (lambdas)
    def test_pickle_json_lambda_dump_load(self):
        self.json_parser.dump(self.json_parser, './Tests/lamb.json', my_p.pack(self.lamb))
        from_json_to_compare = my_p.unpack(self.json_parser.load(self.json_parser, './Tests/lamb.json'))
        self.pickle_parser.dump(self.pickle_parser, './Tests/lamb.pickle', my_p.pack(self.lamb))
        from_pickle_to_compare = my_p.unpack(self.pickle_parser.load(self.pickle_parser, './Tests/lamb.pickle'))
        self.assertEqual(from_json_to_compare(2), from_pickle_to_compare(2))

    def test_json_yaml_lambda_dump_load(self):
        self.json_parser.dump(self.json_parser, './Tests/lamb.json', my_p.pack(self.lamb))
        from_json_to_compare = my_p.unpack(self.json_parser.load(self.json_parser, './Tests/lamb.json'))
        self.yaml_parser.dump(self.yaml_parser, './Tests/lamb.yml', my_p.pack(self.lamb))
        from_yaml_to_compare = my_p.unpack(self.yaml_parser.load(self.yaml_parser, './Tests/lamb.yml'))
        self.assertEqual(from_json_to_compare(2), from_yaml_to_compare(2))

    def test_yaml_toml_lambda_dump_load(self):
        self.yaml_parser.dump(self.yaml_parser, './Tests/lamb.yml', my_p.pack(self.lamb))
        from_yaml_to_compare = my_p.unpack(self.yaml_parser.load(self.yaml_parser, './Tests/lamb.yml'))
        self.json_parser.dump(self.json_parser, './Tests/lamb.toml', my_p.pack(self.lamb))
        from_toml_to_compare = my_p.unpack(self.json_parser.load(self.json_parser, './Tests/lamb.toml'))
        self.assertEqual(from_yaml_to_compare(2), from_toml_to_compare(2))

    def test_yaml_pickle_lambda_dump_load(self):
        self.pickle_parser.dump(self.pickle_parser, './Tests/lamb.pickle', my_p.pack(self.lamb))
        from_pickle_to_compare = my_p.unpack(self.pickle_parser.load(self.pickle_parser, './Tests/lamb.pickle'))
        self.yaml_parser.dump(self.yaml_parser, './Tests/lamb.yml', my_p.pack(self.lamb))
        from_yaml_to_compare = my_p.unpack(self.yaml_parser.load(self.yaml_parser, './Tests/lamb.yml'))
        self.assertEqual(from_pickle_to_compare(2), from_yaml_to_compare(2))


if __name__ == "__main__":
    unittest.main()