"""# NumPy is imported, seed is set
import numpy as np
# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice > 2 and dice < 6 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)
"""
import numpy as np 
x = 1000
while x > 1 :
	print(x)
	x = x -1
	y = np.random.randint(0,x)
	print(',')
	print(y)
