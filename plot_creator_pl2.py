import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from collections import defaultdict


num_of_docs = [413, 3, 1, 16, 1, 13, 4, 6, 2, 92, 19, 1, 124, 1, 21, 46, 2]
list_of_rates = [0, 1.0, 2.0, 3.0, 3.2, 3.5, 3.7, 3.8, 3.9, 4.0, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9]
listRes = list(zip(num_of_docs, list_of_rates))

my_dict = defaultdict(int)

for i in range(0, 5):
    for elem in listRes:
        if((i<=elem[1]) and (elem[1]<(i+1))):
            my_dict[i] += elem[0]
    print(str(i)+" : "+str(my_dict[i]))
width = 0.4


xVals = my_dict.keys()
yVals =  my_dict.values()
label= ['[0-1)','[1-2)','[2-3)','[3-4)','[4-5]']
plt.bar(xVals, yVals, width, align='center')
ax = plt.axes()
ax.set_xticklabels(label)
plt.xlabel('Rate range', fontsize=16)
plt.ylabel('Number of doctors', fontsize=16)
major_ticks_x = np.arange(min(xVals),max(xVals)+1 , 1)
minor_ticks_y = np.arange(min(yVals),max(yVals)+1 , 10)
major_ticks_y = np.arange(min(yVals),max(yVals)+1 , 1)
ax.set_yticks(minor_ticks_y, minor=True)
ax.set_xticks(major_ticks_x)
plt.title('Number of doctors in each rating range')
plt.grid(True, lw = 0.8, ls = '--', c = '.75')
plt.savefig('rating_range.png')
plt.show()