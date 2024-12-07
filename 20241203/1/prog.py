class dump(type):
    def __new__(cls, name, prts, dct):
        for atr_name, atr_val in dct.items():
            if callable(atr_val):
                orig = atr_val
                
                def wrapper(meth_name, method):
                    def wrp_meth(self, *args, **kwargs):
                        print(f"{meth_name}: {args}, {kwargs}")
                        return method(self, *args, **kwargs)
                    return wrp_meth
                
                dct[atr_name] = wrapper(atr_name, orig)
        return super().__new__(cls, name, prts, dct)

import sys
exec(sys.stdin.read())

