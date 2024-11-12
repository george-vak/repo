class A: pass
class B: pass

class C(B, A): pass
class D(A, B): pass

# class E(C, D): pass
# class E(A, C): pass
# class E(D, C): pass
