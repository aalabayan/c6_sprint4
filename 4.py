from time import sleep
import numpy as np
import random

def get_random_number():
	return random.randint(1,5)

def delay(seconds):
	print(f"Sleeping for {seconds} second(s)")
	sleep(seconds)  
	
def main():
	for i in np.arange(0,5):
		print (i)
		delay(seconds=get_random_number())
		
if __name__ == "__main__":
	main()