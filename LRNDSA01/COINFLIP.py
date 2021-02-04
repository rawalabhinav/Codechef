def result(i,n,q) :
	if n%2 == 0:
		r = (n+1)//2
	elif i == 1 :
		if q == 1 :
			r = (n-1)//2
		else :
			r = (n+1)//2
	else :
		if q == 1 :
			r = (n +1)//2
		else :
			r = (n-1)//2
	return r

arr = []
for a in range(int(input())):
	for b in range(int(input())) :
		i, n, q = map(int, input().split())
		arr.append(result(i,n,q))
for c in arr :
	print(c)
