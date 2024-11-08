class Omnibus:
    attrs = {}

    def __setattr__(self, name, val):
        if not name.startswith("_"):
            code = id(self)
            if name not in self.__dict__:
                if name in Omnibus.attrs:
                    if code not in Omnibus.attrs[name]:
                        Omnibus.attrs[name].append(code)
                else:
                    Omnibus.attrs[name] = [code]

    def __getattr__(self, name):
        if name in Omnibus.attrs:
            return len(Omnibus.attrs[name])
        return 0

    def __delattr__(self, name):
        code = id(self)
        if name in Omnibus.attrs and code in Omnibus.attrs[name]:
            Omnibus.attrs[name].remove(code)
            if not Omnibus.attrs[name]:
                del Omnibus.attrs[name]

import sys
exec(sys.stdin.read())

