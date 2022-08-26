import numpy as np 
import time
#Fix this program so that it doesn't print only one number
x = np.random.randint(1,999999999999)
while x > 0 : 
	if x%2 == 0 :
		print(x)
		print( 'which is even')
		print("")
		time.sleep(1/100)
	else :
		print(x)
		print( 'which is not even')
		print("")
		time.sleep(1/100)
