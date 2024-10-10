import matplotlib.pyplot as plt
import numpy as np
month=(['JAN','FEB','MAR','ARR','MAY','JUN','JLY','AUG','SEP','OCT','NOV','DEC'])
AS=np.array([173,153,195,147,120,144,148,109,174,130,172,131])
LS=np.array([189,189,105,112,173,109,151,197,174,145,177,161])
SLS=np.array([185,185,126,134,196,153,112,133,200,145,167,110])

plt.plot(month,AS,label='Affordable segment',color='pink',linestyle='--')
plt.plot(month,LS,label='Luxury Segment',color='yellow',linestyle='-.')
plt.plot(month,SLS,label='Super Luxury Segment',color='blue',linestyle=':')

plt.xlabel('Month of Year',fontsize=18)
plt.ylabel('Label of Segment')

plt.title('Sale Data')
plt.title('ANANDHU \n 23MCA015',loc='right')

plt.show()