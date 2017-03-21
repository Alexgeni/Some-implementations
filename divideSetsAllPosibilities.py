#getting subsets
def cal(i,L,cset,comp,mySet):
	for n in range(i,len(L)):
		if sum(cset+[L[n]])==sum(L)/2:#save subsets that their sum are equal to half the original set
			mySet.append(cset+[L[n]])
		comp.append(cset+[L[n]])
		cal(n+1,L,comp[len(comp)-1],comp,mySet)
	if len(mySet)>0 and i==0:
		return mySet
	else:
		return False
#filter possibilities in set1 and set2
def getSubsets(L):
	L.sort()
	subSets=cal(0,L,[],[],[])
	if subSets:
		set2=[]
		set1=[]
		for subset in subSets:
			if checkSimilarity(subset,set1) is False and checkSimilarity(subset,set2) is False:
				set2.append(L.copy())
				set1.append(subset.copy())
				for n in subset:
					set2[len(set2)-1].remove(n)
		return [set1,set2]
	else:
		return False
#check similar sets to ignore them
def checkSimilarity(s1,s2):
	for subset in s2:
		if subset==s1:
			return True
	return False
#Running code
L=[1,1,1]
subSets=getSubsets(L)
if subSets:
	print("The all possible 2 equal subsets are :")
	for index in range(0,len(subSets[0])):
		print("Set1: ",subSets[0][index]," Set2: ",subSets[1][index])			
else:
	print("Can't be divided to any two equal subsets")
