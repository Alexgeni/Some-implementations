def divideSets(L):#linear splitting sets
	L.sort(reverse=True)
	set1=[]
	set2=[]
	for i in L:
		if sum(set1) < sum(set2):
			set1.append(i)
		else:
			set2.append(i)
	print("List : ",L,"Set 1 is ",set1,"\nSet 2 is ",set2)
n=int(input("List's size"))
L=[]
for i in range(0,n):
	L.append(int(input()))
#L=[1,2,2,4,1,5]
divideSets(L)
