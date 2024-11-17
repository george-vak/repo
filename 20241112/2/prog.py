import re
class InvalidInput(Exception):
    pass
class BadTriangle(Exception):
    pass

def correct_input(inp):
    pattern = r"\(\s*(.+?)\s*,\s*(.+?)\s*\),\s*\(\s*(.+?)\s*,\s*(.+?)\s*\),\s*\(\s*(.+?)\s*,\s*(.+?)\s*\)"
    match = re.fullmatch(pattern, inp)
    if not match:
        raise InvalidInput()
    return list(match.groups())

def is_triag(x1, y1, x2, y2, x3, y3):
    if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
        raise BadTriangle()
    return True

def to_nums(arr):
    nums = []
    for el in arr:
        try:
            nums.append(float(el))
        except ValueError:
            raise BadTriangle()
    return nums

def triangleSquare(s):
    x1, y1, x2, y2, x3, y3 = to_nums(correct_input(s))
    if is_triag(x1, y1, x2, y2, x3, y3):
        print(abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
        exit()



while True:
    try:
        string = input()
        triangleSquare(string)
    except InvalidInput: print("Invalid input")
    except BadTriangle: print("Not a triangle")


