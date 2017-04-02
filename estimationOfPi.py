import random
import math
def estimatePi(itt):
	hits=0 # number of hits
	for i in range(0,itt):
		x=random.uniform(0,1)
		y=random.uniform(0,1)
		z=x*x+y*y #Pythagorean Theorum
		if math.sqrt(z)<=1: #if point(x,y)lies within the triangle
			hits=hits+1
	return (hits*4)/itt #return The estimation of pi is 4*hits/shots
itt=100 #itterations
pi = estimatePi(itt)
print("Pi : ",pi)
