class Doubleton(type):
    _instances = []
    _counter = 1

    def __call__(cls, *args, **kwargs):
        if len(cls._instances) < 2:
            cls._instances.append(super().__call__(*args, **kwargs))
        cls._counter += 1
        return cls._instances[cls._counter % len(cls._instances)]

class D(metaclass=Doubleton):
    pass

print(*(D() for _ in range(7)), sep='\n')

