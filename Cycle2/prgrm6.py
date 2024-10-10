print(" ANANDHU V POOVANKAL")
print(" 23mca015")
import numpy as np
two_d_array=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
excld_fst_row=two_d_array[1:]
excld_lst_clm=two_d_array[:,:-1]
clm_1_2_in_row_2_3=two_d_array[1:3,0:2]
clmn_2_3=two_d_array[:,1:3]
element_2_3_in_fst_row=two_d_array[0,1:3]
decnt_ordr=two_d_array.ravel()[::-1][4:11]
print("Orginal 2D Array:",two_d_array)
print("Element Excluding in first row \n",excld_fst_row)
print("Element Exclude in Last Columb:\n",excld_lst_clm)
print("Elements in the 1st and 2nd colum in 2 and 3 rd row:\n",clm_1_2_in_row_2_3)
print("Elemts of the 2 nd and 3rd row:\n",clmn_2_3)
print("2 nd and 3 rd element os the 1st row:\n",element_2_3_in_fst_row)
print("Elements in descending ordr:\n",decnt_ordr)