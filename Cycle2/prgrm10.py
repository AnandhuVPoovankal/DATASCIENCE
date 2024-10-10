print(" ANANDHU V POOVANKAL")
print(" 23mca015")
import numpy as np
matrix_size=3
matrix=np.random.randint(10,20,size=(matrix_size,matrix_size))
print("Orginal Matrix:\n",matrix)
if np.linalg.matrix_rank(matrix)==matrix_size:
    inverse_matrix=np.linalg.inv(matrix)
    print("Inverse Matrix:\n",inverse_matrix)
else:
    print("The matrix i not invertible(its rank is less than the size).")
rank=np.linalg.matrix_rank(matrix)
print("Rnak of the matrix:",rank)
determinant=np.linalg.det(matrix)
print("Determinent of the matrix:",determinant)
matrix_1d=matrix.flatten()
print("Matrix as 1d:",matrix_1d)
eigevalues,eigenvectors=np.linalg.eig(matrix)
print("Eigen values:\n",eigevalues)
print("eigen vectors:\n",eigenvectors)

