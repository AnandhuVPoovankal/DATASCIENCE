print(" ANANDHU V POOVANKAL")
print(" 23mca015")
import numpy as np
A=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30]])
print("Matrix A is:\n",A)
B=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Matrix B is:\n",B)
sub_matrix=A[:3,:3]
print("The sub Matrix is:\n",sub_matrix)
result=np.dot(sub_matrix,B)
print("Matrix after multiplication with the sub matrix of A and matrix B:")
print(result)
A[:3,:3]=result
print("Matrix A after the operation:\n",A)
