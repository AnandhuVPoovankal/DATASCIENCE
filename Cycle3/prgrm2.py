import matplotlib.pyplot as plt
day=['Mon','Tues','Wed','Thurs','Fri']
drinks_sales=[300,450,150,400,650]
food_sales=[400,500,350,300,500]
fig,axs=plt.subplots(2,1,figsize=(8,8))
axs[0].plot(day,drinks_sales,linestyle='--',color='cyan',marker='H',markersize=8,markerfacecolor='magenta',markeredgecolor='black')
axs[0].set_xlabel('Days of Week')
axs[0].set_ylabel('Sale of Drinks')
axs[0].set_title('Sale Data1',loc='right')
axs[0].set_title('ANANDHU \n 23MCA015',loc='left')
axs[0].grid(True,color='blue',linestyle='dotted')

axs[1].plot(day,food_sales,linestyle='-',color='yellow',marker='D',markersize=8,markerfacecolor='green',markeredgecolor='red')
axs[1].set_xlabel('Days of Week')
axs[1].set_ylabel('Sale of Food')
axs[1].set_title('Sales Data2',loc='center')
axs[1].grid(True,color='blue',linestyle='dotted')
plt.tight_layout()
plt.show()