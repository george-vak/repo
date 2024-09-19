from itertools import filterfalse


def A(n):
    if n % 2 == 0 and n % 25 == 0: return True
    return False

def B(n):
    if n % 2 != 0 and n % 25 == 0: return True
    return False

def C(n):
    if n % 8: return False
    return True

def analyse(n):
    match A(n), B(n), C(n):

        case True, False, True:
            print("A + B - C +")

        case True, False, False:
            print("A + B - C -")

        case False, True, True:
            print("A - B + C +")

        case False, True, False:
            print("A - B + C -")

        case False, False, False:
            print("A - B - C -")

analyse(int(input()))
