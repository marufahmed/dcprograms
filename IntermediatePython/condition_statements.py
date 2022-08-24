import time
for x in range(1000) : 
	if x%2 == 0 :
		print(x)
		print( 'which is even')
		print("")
		time.sleep(1/10)
	else :
		print(x)
		print( 'which is not even')
		print("")
		time.sleep(1/10)
