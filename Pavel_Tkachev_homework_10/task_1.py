class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        result = ''
        for row in self.matr:
            for i in row:
                result += f'{i}  '
            result += '\n'
        return result

    def __add__(self, other):
        result = ''
        for i in range(len(self.matr)):
            for j in range(len(self.matr[i])):
                result += f'{self.matr[i][j] + other.matr[i][j]}  '
            result += '\n'
        return result


m1 = Matrix([[31, 22], [37, 43], [51, 86]])
print(m1)
m2 = Matrix([[3, 5, 32], [2, 4, 6]])
m3 = Matrix([[3, 5, 32], [2, 4, 6]])
print(m2)
print(m3)
print(m2 + m3)
