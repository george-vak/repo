from decimal import Decimal
from fractions import Fraction

def multiplier(x, y, Type):
    return Type(x) * Type(y)

print(multiplier('1/6', '2/3', Fraction))
print(multiplier('3.6', '1.1', float))
print(multiplier('3.6', '1.1', Decimal))
