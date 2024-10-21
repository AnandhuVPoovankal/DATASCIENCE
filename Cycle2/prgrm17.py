print(" ANANDHU V POOVANKAL")
print(" 23mca015")
import numpy as np
A=np.array([[5,27,32],[14,53,62],[67,88,19]])
U,S,VT=np.linalg.svd(A)
A_hat=U@np.diag(S)@VT
print("Orginal Matrix A:\n",A)
print("Singular Values:\n",S)
print("Reconstructed Matrix A_hat:\n",A_hat)