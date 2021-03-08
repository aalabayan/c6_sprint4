from time import sleep
import numpy as np

def delay(seconds):
	print(f"Sleeping for {seconds} second(s)")
	sleep(seconds)
	
def main():
	for i in np.arange(0,5):
		print('i')
		delay(seconds=2)
		
if __name__ == "__main__":
	main()