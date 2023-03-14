import numpy as np
import random
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
    return np.subtract(matrix1, matrix2).tolist()


def matrix_multiplication(matrix1, matrix2):
    return np.matmul(matrix1, matrix2).tolist()


def matrix_dot_product(matrix1, matrix2):
    return np.dot(matrix1, matrix2).tolist()


def matrix_determinant(matrix):
    return np.linalg.det(matrix).tolist()


def matrix_inverse(matrix):
    return np.linalg.inv(matrix).tolist()


def matrix_eigenvalues(matrix):
    return np.linalg.eig(matrix)[0].tolist()


def matrix_eigenvectors(matrix):
    return np.linalg.eig(matrix)[1].tolist()

def rand(rows, cols): 
    arr = []
    for row in range(rows):
        arr.append([])
        for col in range(cols):
            arr[row].append(random.randint(0,9))
    return np.array(arr).tolist()

print(matrix_eigenvalues([[1,2,3], [3,2,1], [2,1,3]]))
# m1 = Matrix(3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# m2 = Matrix(3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(matrix_addition(m1, m2))
