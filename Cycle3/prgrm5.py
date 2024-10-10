import matplotlib.pyplot as plt
import numpy as np
mode_transport=np.array(['Walking','Cycling','Car','Bus','Train'])
feq=np.array([29,15,35,18,3])
plt.xlabel('Mode of Transport')
plt.ylabel("Frequence")
plt.title('ANANDHU \n 23MCA015',loc='right')
plt.bar(mode_transport,feq,width=0.1,color='green')
plt.show()

