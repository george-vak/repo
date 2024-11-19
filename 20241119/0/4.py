class Counter:
    def __init__(self):
        self.value = 0

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value


class C:
    counter = Counter()
    def __init__(self):
        self.counter += 1
    def __del__(self):
        self.counter -= 1

c = C()
print(c.counter)

d = C()
print(d.counter)

del c
print(d.counter)

