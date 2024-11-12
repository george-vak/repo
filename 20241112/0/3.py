class A:
    _v = 0
    def inc(self):
        self._v += 1
        print(self._v)
class B(A):
    _v = 100500

b = B()
b.inc()
b.v = 42
print(b.v)
print(dir(B))
