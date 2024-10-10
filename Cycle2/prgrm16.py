import numpy as np
A=np.array([[2,-2,2],[3,0,1],[1,1,-1]])
B=np.array([-3,5,-2])
X=np.linalg.solve(A,B)
print("Matrix A:\n",A)
print("Vector b:",B)
print("Solution for X:",X)