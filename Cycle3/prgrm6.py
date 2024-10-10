import matplotlib.pyplot as plt
import numpy as np
x=([61,63,64,66,68,69,71,71.5,72,72.5,73,73.5,74,74.5,76,76.2,76.5,77,77.5,78,78.5,79,79.2,80,81,82,83,84,85,87])
plt.hist(x,bins=range(40,110,5),)
plt.title('Cherry tree height',loc='left')
plt.title('Anandhu \n 23mca0150',loc='right')
plt.xlabel('Height in (inch)')
plt.ylabel("Frequency")
plt.show()