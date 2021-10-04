class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        return self.number - other.number

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        return round(self.number / other.number)

kletka1 = Cell(8)
kletka2 = Cell(10)
print(kletka1 + kletka2)
print(kletka1 - kletka2)
print(kletka1 * kletka2)
print(kletka1 / kletka2)