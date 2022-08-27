import numpy as np


matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)
print(matrix[0, 1])
print(matrix @ matrix)
print(matrix.shape)
print(matrix.diagonal())
print(matrix.flatten())
print(matrix.transpose())
print(matrix.min())
print(matrix.max())
print(matrix.mean())
print(matrix.sum())

my_matrix1 = np.array([[1, 2], [3, 4]])
my_matrix2 = np.array([[2, 0], [1, 2]])
print(my_matrix1 @ my_matrix2)
print(np.vstack([my_matrix1, my_matrix2]))
print(np.hstack([my_matrix1, my_matrix2]))
print(my_matrix1.reshape(1, 4))

print(np.arange(1, 24, 2).reshape(3, 2, 2))

print(np.random.random([3, 3]))
