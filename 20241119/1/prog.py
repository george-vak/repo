def objcount(cls):
    cls.counter = 0
    orig_init = getattr(cls, "__init__", None)
    orig_del = getattr(cls, "__del__", None)

    def new_init(self, *args, **kwargs):
        cls.counter += 1
        if orig_init:
            orig_init(self, *args, **kwargs)

    def new_del(self):
        cls.counter -= 1
        if orig_del:
            orig_del(self)

    cls.__init__ = new_init
    cls.__del__ = new_del

    return cls

import sys
exec(sys.stdin.read())
