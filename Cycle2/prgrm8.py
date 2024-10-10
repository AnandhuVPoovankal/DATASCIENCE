print(" ANANDHU V POOVANKAL")
print(" 23mca015")
import numpy as np
ary_1d=np.array([1,2,3,4,5])
print("1D Aaray before insertion:\n",ary_1d)
ary_1d=np.insert(ary_1d,2,6)
print("1D Array after insertion:\n",ary_1d)
ary_2d=np.array([[1,2,3],[4,5,6]])
print("2D Array before insertion:\n",ary_2d)
ary_2d=np.insert(ary_2d,1,[7,8,9],axis=0)
print("2D Array after insertion:\n",ary_2d)

