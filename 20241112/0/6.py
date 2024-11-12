class A:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f"<{self.val}>"

class B(A):
    def __init__(self, val):
        super().__init__(val)
        self.val += 1

print(A(9))
print(B(9))
