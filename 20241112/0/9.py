def divisor(a, b):
    try:
        if b < 3:
            raise ZeroDivisionError("maloe b")
        return a / b
    except ZeroDivisionError as ex:
        return ex


print(divisor(10, 5))
print(divisor(3, 1))
