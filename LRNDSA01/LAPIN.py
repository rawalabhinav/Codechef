def sort(x,y,z) :
	w = sorted(x[y:z])
	w.sort()
	w = ''.join(w)
	return w
strings = []
T = int(input())
for i in range(T):
	strings.append(input())
for j in strings:
	if  sort(j,0,len(j)//2) == sort(j,(len(j) +1)//2, len(j) +1) :
		print("YES")
	else :
		print("NO")
