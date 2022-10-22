# %%
#import relevant libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('coding-environment-exercise.csv')
data.head()

plt.plot(data['date'],data['value'])

# naming the x axis 
plt.xlabel('date') 

# naming the y axis 
plt.ylabel('value')

# naming the xticks
#plt.xticks(list())

# naming the yticks 
plt.ylabel('y - axis') 

# function to show the plot 
plt.show() 


#Saving the plot as an image
plt.savefig('first plot.jpg', bbox_inches='tight', dpi=150)




