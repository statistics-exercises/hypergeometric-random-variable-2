import matplotlib.pyplot as plt
import numpy as np

def choice_with_replacement( M, R, N ) : 
  # Your code goes here 
  
  
  
# You shouldn't need to modify anything from here onwards this just plots your variable
xvals, yvals = np.zeros(100), np.zeros(100) 
for i in range(100) : xvals[i], yvals[i] = i+1, choice_with_replacement(4,4,12)

plt.plot( xvals, yvals, 'ko' )
plt.savefig("choice_var.png")
