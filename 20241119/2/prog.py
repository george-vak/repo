class Num:
    def __init__(self, default=0):
        self.default = default
        self.stor = f"my_field"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.stor, self.default)

    def __set__(self, instance, val):
        if hasattr(val, 'real'):
            setattr(instance, self.stor, val.real)
        elif hasattr(val, '__len__'):
            setattr(instance, self.stor, len(val))


    def __delete__(self, instance):
        setattr(instance, self.stor, self.default)



import sys
exec(sys.stdin.read())



