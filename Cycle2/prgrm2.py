print(" ANANDHU V POOVANKAL")
print(" 23mca015")
import numpy as np
arr=np.array([[1+2j,3+4j,5+6j],[7+8j,9+1j,11+22j]],dtype=complex)
print("Complex array:")
print(arr)
row,coloums=arr.shape
print("Rows:",row)
print("Coloums:",coloums)
dimensions=arr.ndim
print("dimensionds:",dimensions)
reshaped_arr=arr.reshape(3,2)
print("reshaped array:",reshaped_arr)