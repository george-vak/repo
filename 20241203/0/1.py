C = type("C", (), {"f": 123, "__init__": lambda self, x: setattr(self, "var", x), "var": 100500})
c = C(45)
print(c.var)
