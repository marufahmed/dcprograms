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
import time
step = 1000
if step > 1:
	print(step)
	step = step - 1 
	print(np.random.randint(1,1000)
    	#time.sleep(1/100)
print('end of program')
