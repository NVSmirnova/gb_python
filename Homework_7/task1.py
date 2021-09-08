class Matrix:
    def __init__(self, values):
        self.values = values
    def __add__(self, other):
        mt = []
        for i in range(0, len(self.values)):
            line = []
            for j in range(0, len(self.values[1])):
                line.append(self.values[i][j] + other.values[i][j])
                #print(f"line is {line}")
            mt.append(line)
        #print(mt)
        return Matrix(mt)

    def __str__(self):
        otv = ""
        for i in range(0, len(self.values)):
            otv += f"{self.values[i]}\n"
        #return f'{self.values}'
        return otv


mt1 = Matrix([[1, 2], [3, 4]])
#print(mt1.values)
mt2 = Matrix([[10, 20], [30, 40]])
print(mt1 + mt2)

mt1 = Matrix([[10, 20, 30, 40], [300, 400, 500, 600], [1, 2, 3, 4]])
#print(mt1.values)
mt2 = Matrix([[100, 200, 300, 400], [3000, 4000, 5000, 6000], [10, 20, 30, 40]])
print(mt1 + mt2)