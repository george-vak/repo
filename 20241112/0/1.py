class A:
    v = 1

class B(A):
    v = 2

b = B()
b.v = 3

print("до", b.v)

del b.v
print("удал из экземпл", b.v)

del B.v
print("из класса", b.v)

