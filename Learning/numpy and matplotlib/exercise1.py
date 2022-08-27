import numpy as np


first_matrix = np.arange(3, 12).reshape(3, 3)

print(first_matrix.min())
print(first_matrix.max())
print(first_matrix.mean())

second_matrix = first_matrix ** 2
third_matrix = np.vstack([first_matrix, second_matrix])
print(third_matrix @ first_matrix)
print(third_matrix.reshape(3, 3, 2))
