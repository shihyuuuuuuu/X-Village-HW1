import random

from copy import deepcopy


class Matrix:

    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        self.mat = []
        self.row = nrows
        self.col = ncols
        for i in range(nrows):
            temp = []
            for j in range(ncols):
                temp.append(random.randint(0, 9))
            self.mat.append(temp)
        pass

    def add(self, m):
        self.result = [[0 for x in range(self.col)] for y in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                self.result[i][j] = self.mat[i][j] + m[i][j]
        return self.result
        pass

    def sub(self, m):
        self.result = [[0 for x in range(self.col)] for y in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                self.result[i][j] = self.mat[i][j] - m[i][j]
        return self.result
        pass

    def mul(self, m):
        self.result = [[0 for x in range(len(m[0]))] for y in range(self.row)]
        for k in range(len(m[0])):
            for i in range(self.row):
                temp = 0
                for j in range(self.col):
                    temp += self.mat[i][j] * m[j][k]
                self.result[i][k] = temp
        return self.result
        pass

    def transpose(self):
        self.result = [[0 for x in range(len(mul_result[0]))] for y in range(len(mul_result))]
        for i in range(len(mul_result)):
            for j in range(len(mul_result[0])):
                self.result[j][i] = mul_result[i][j]
        pass
    
    def display(self, n):
        """Display the content in the matrix"""
        if n == 0:
            toprint = self.mat.copy()
        elif n == 1:
            toprint = self.result.copy()
        for i in range(len(toprint)):
            for j in range(len(toprint[0])):
                print(toprint[i][j], end = " ")
            print()
        print()
        pass

a_row = int(input("Enter A matrix's rows: "))
a_col = int(input("Enter A matrix's cols: "))
a = Matrix(a_row, a_col)
print("Matrix A(" + str(a_row) + ", " + str(a_col) + "):")
a.display(0)


b_row = int(input("Enter B matrix's rows: "))
b_col = int(input("Enter B matrix's cols: "))
b = Matrix(b_row, b_col)
print("Matrix B(" + str(b_row) + ", " + str(b_col) + "):")
b.display(0)

print("========== A + B ==========")
add_esult = a.add(b.mat)
a.display(1)

print("========== A - B ==========")
sub_result = a.sub(b.mat)
a.display(1)

print("========== A * B ==========")
mul_result = a.mul(b.mat)
a.display(1)

print("===== the transpose of A * B =====")
trans_result = a.transpose()
a.display(1)


