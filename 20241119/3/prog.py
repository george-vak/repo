class Alpha:
    __slots__ = [chr(i) for i in range(ord('a'), ord('z') + 1)]

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.__slots__:
                setattr(self, key, value)
            else:
                raise AttributeError(f"no such attr'{key}'")


    def __str__(self):
        return ', '.join(f"{key}: {getattr(self, key)}" for key in sorted(self.__slots__)
                         if hasattr(self, key))


class AlphaQ:
    _valid_keys = {chr(i) for i in range(ord('a'), ord('z') + 1)}

    def __init__(self, **kwargs):
        self._attributes = {}
        for key, value in kwargs.items():
            try:
                if key in self._valid_keys:
                    self._attributes[key] = value
                else:
                    raise AttributeError
            except AttributeError:
                print(f"параматр <{key}> не поддерживается и был пропущен")

    def __setattr__(self, name, value):
        if name == "_attributes" or name == "_valid_keys":
            super().__setattr__(name, value)
        elif name in self._valid_keys:
            self._attributes[name] = value
        else:
            raise AttributeError(f"no such attr '{name}'")

    def __getattr__(self, name):
        if name in self._attributes:
            return self._attributes[name]
        raise AttributeError(f"no such attr '{name}'")

    def __str__(self):
        return ', '.join(f"{key}: {value}" for key, value in sorted(self._attributes.items()))


import sys
exec(sys.stdin.read())


