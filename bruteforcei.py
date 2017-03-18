def calculateDeltaX(x):
	#print(x)
	dx=[]
	for i in range(0,len(x)-1):
		for j in range(i+1,len(x)):
			n=x[j]-x[i]
			dx.append(n)
	dx.sort(key=int)
	#print("dx = ",dx)
	return dx
def BruteForcePDP(L,n):
	L.sort(key=int)
	M=max(L)
	s=list(range(0,M+1))
	#print("s=",s)
	dx=[]
	print(s[1:M-1])
	subsets=getSubsets(s[1:M-1], n-2)
	for subset in subsets:
		print(subset)
		x=list(subset)
		x.insert(0,0)
		x.insert(n,M)
		dx=calculateDeltaX(x)
		if(dx==L):
			print("FOUND \n x = ",x) 
			return
	print("no solution")
def getSubsets(lista, r):
    pool = tuple(lista)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
BruteForcePDP([2,2,2,4,4,4,6,6,8,10],5)
