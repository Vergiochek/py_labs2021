import pickle
from my_p import MyParser


class PickleParser(MyParser):
    def dump(self, save_file_path, obj):
        with open(save_file_path, 'wb') as file:
            pickle.dump(obj, file, protocol=pickle.HIGHEST_PROTOCOL)

    def dumps(self, obj):
        return pickle.dumps(obj)

    def load(self, fp):
        with open(fp, 'rb') as file:
            return pickle.load(file)

    def loads(self, data):
        return pickle.loads(data)