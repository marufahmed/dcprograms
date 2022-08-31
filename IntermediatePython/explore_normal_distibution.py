import numpy as np
import matplotlib.pyplot as plt
#needs to have an input from user to set feed and number of iterations and check the distribution
x = []
y = 100000
while y > 1 :
    x.append(np.random.randint(1,100))
    y = y-1

print(x)
plt.hist(x)

#%%
