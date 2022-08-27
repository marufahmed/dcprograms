import numpy as np
import matplotlib.pyplot as plt
x = []
y = 100000
while y > 1 :
    x.append(np.random.randint(1,100))
    y = y-1

print(x)
plt.hist(x)
