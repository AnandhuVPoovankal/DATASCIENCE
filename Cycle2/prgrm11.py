import numpy as np
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
x_cube_mutiply=np.multiply(x,np.multiply(x,x))
x_cube_operator=x*x*x
x_cube_power=np.power(x,3)
x_cube_double_star=x**3
identity_matrix=np.identity(x.shape[0])
x_cube_power_2=np.power(x,2)
x_cube_power_3=np.power(x,3)
x_cube_power_4=np.power(x,4)
print("Orginal Matrix:\n",x)
print("Cube Matrix (Method 1- multiply()):\n",x_cube_mutiply)
print("Cube Matrix (Method 2 - * Opeerator):\n",x_cube_operator)
print("Cube Matrix (Method 3 -Power):\n",x_cube_double_star)
print("Identity Matrix:\n",identity_matrix)
print("Matrix to differnt Powers:")
print("X^2:\n",x_cube_power_2)
print("X^3:\n",x_cube_power_3)
print("X^4:\n",x_cube_power_4)