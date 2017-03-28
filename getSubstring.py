#return the indeces of substrings in the string
def getIndeces(indeces,i,s,sub):
	if i <= (len(s)-len(sub)):
		if nextIndex(sub,s,i):
			indeces.append(i)
			getIndeces(indeces,i+len(sub),s,sub)
		else:
			getIndeces(indeces,i+1,s,sub)
	return indeces
#Is the string carring more substrings ?
def nextIndex(sub,string,i):
	for j in range(0,len(sub)):
		if string[i+j] == sub[j]:
			continue
		else:
			return False
	return True
myString=""
substring=""
while  myString=="":
	myString=input("Enter long string: ")
while substring=="":
	substring=input("Substring: ")
ind = getIndeces([],0,myString,substring)
print(ind)
