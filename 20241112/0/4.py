m = type("C", (),
         {
    "a": 100500,
    "fun": lambda self: self.a,
    "__init__": lambda self, val: setattr(self, 'val', val)
         })

print(m(5).val)

