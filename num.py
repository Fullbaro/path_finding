import decimal

# This class needed for fixing the Floating Point Arithmetic Precision Error
class Num(float):

    def __init__(self, value):
        self.value = decimal.Decimal(str(value))

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __add__(self, other):
        return Num(self.value + Num(other).value)

    def __sub__(self, other):
        return Num(self.value - Num(other).value)

    def __mul__(self, other):
        return Num(self.value * Num(other).value)

    def __truediv__(self, other):
        return Num(self.value / Num(other).value)

    def __pow__(self, other):
        return Num(self.value ** Num(other).value)