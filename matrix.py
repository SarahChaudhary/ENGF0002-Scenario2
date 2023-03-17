import numpy as np
import random
class Matrix:
    # values is 2d list
    def __init__(self, size, values):
        self.size = size
        self.values = values

    def __str__(self):
        return str(self.values)

def correct_num_values(mat):
    for i in mat:
        if None in i:
            raise ValueError("expected more input values")
        
def matrix_addition(matrix1, matrix2):
    correct_num_values(matrix1)
    correct_num_values(matrix2)
    return np.add(matrix1, matrix2).ravel().tolist()



def matrix_subtraction(matrix1, matrix2):
    correct_num_values(matrix1)
    correct_num_values(matrix2)
    return np.subtract(matrix1, matrix2).ravel().tolist()


def matrix_multiplication(matrix1, matrix2):
    correct_num_values(matrix1)
    correct_num_values(matrix2)
    return np.matmul(matrix1, matrix2).ravel().tolist()


def matrix_dot_product(matrix1, matrix2):
    correct_num_values(matrix1)
    correct_num_values(matrix2)
    return np.dot(matrix1, matrix2).ravel().tolist()


def matrix_determinant(matrix):
    correct_num_values(matrix)
    return np.linalg.det(matrix).ravel().tolist()


def matrix_inverse(matrix):
    correct_num_values(matrix)
    if matrix_determinant(matrix) // 1 == 0:
        raise ValueError("matrix is not invertible")
    return np.linalg.inv(matrix).ravel().tolist()


def matrix_eigenvalues(matrix):
    correct_num_values(matrix)
    return np.linalg.eig(matrix)[0].tolist()


def matrix_eigenvectors(matrix):
    correct_num_values(matrix)
    return np.linalg.eig(matrix)[1].tolist()

def rand(rows, cols): 
    arr = []
    for row in range(rows):
        arr.append([])
        for col in range(cols):
            arr[row].append(random.randint(0,9))
    return np.array(arr).ravel().tolist()

#print(matrix_multiplication([[1,2,3], [4,5,6],[7,8,9]],[[1,2,3], [4,5,6],[7,8,None]]))