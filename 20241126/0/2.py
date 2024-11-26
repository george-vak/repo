import pickle

class SerCls:
    def __init__(self, lst, dct, num, st):
        self.lst = lst
        self.dct = dct
        self.num = num
        self.st = st

ser = SerCls([1, 2, 3], {"key": "value"}, 42, "example")
serialized_data = pickle.dumps(ser)
print(serialized_data)
del ser
ser1 = pickle.loads(serialized_data)


