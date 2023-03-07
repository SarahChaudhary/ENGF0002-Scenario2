class Matrix:
    # values is 2d list
    def __init__(self, size, values):
        self.size = size
        self.values = values

    def __str__(self):
        return str(self.values)


def matrix_addition(matrix1, matrix2):
    if matrix1.size != matrix2.size:
        return None
    result = []
    for i in range(matrix1.size):
        row = []
        for j in range(matrix1.size):
            row.append(matrix1.values[i][j] + matrix2.values[i][j])
        result.append(row)
    return Matrix(matrix1.size, result)


def matrix_subtraction(matrix1, matrix2):
    pass


def matrix_multiplication(matrix1, matrix2):
    pass


def matrix_dot_product(matrix1, matrix2):
    pass


def matrix_determinant(matrix):
    pass


def matrix_inverse(matrix):
    pass


def matrix_eigenvalues(matrix):
    pass


def matrix_eigenvectors(matrix):
    pass


# m1 = Matrix(3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# m2 = Matrix(3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(matrix_addition(m1, m2))
