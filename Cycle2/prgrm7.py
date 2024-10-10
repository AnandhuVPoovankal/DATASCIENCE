print(" ANANDHU V POOVANKAL")
print(" 23mca015")
import numpy as np
mtrx1=np.array([[1,2,3],[4,5,6],[7,8,9]])
mtrx2=np.array([[9,8,7],[6,5,4],[3,2,1]])
mtrx_sum=mtrx1+mtrx2
mtrx_dif=mtrx1-mtrx2
mtrx_prdct=mtrx1*mtrx2
mtrx_div=mtrx1/mtrx2
mtrx_multiplay=np.dot(mtrx1,mtrx2)
mtrx_transpose=np.transpose(mtrx1)
dignl_sum=np.trace(mtrx1)
print("Matrix 1:\n",mtrx1)
print("Matrix 2:\n",mtrx2)
print("Matrix sum:\n",mtrx_sum)
print("Matrix differnce:\n",mtrx_dif)
print("Matrix Element vise product:\n",mtrx_prdct)
print("Matrix Element vise division:\n",mtrx_div)
print("Matrix Multipilication:\n",mtrx_multiplay)
print("Trancepose of Matrix1:\n",mtrx_transpose)
print("Sum of diagonal elements of matrix1:",dignl_sum)