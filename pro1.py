import random
import math
def estimatePi(error):
	itt=1000 #itterations
	previousPI=0
	while True:
		hits=0 # number of hits
		for i in range(0,itt):
			x=random.uniform(0,1)
			y=random.uniform(0,1)
			z=x*x+y*y #Pythagorean Theorum
			if math.sqrt(z)<=1: #if point(x,y)lies within the triangle
				hits=hits+1
		currentPI=(hits*4)/itt
		#print(currentPI)
		if previousPI==0:
			previousPI=currentPI
			continue
		if (math.fabs(previousPI-currentPI)<error) is True:
			return currentPI#return The estimation of pi is 4*hits/shots
		previousPI=(currentPI+previousPI)/2	
		#previousPI=currentPI
error=float(input("Enter the error value :"))
pi = estimatePi(error)
print("Pi : ",pi)
