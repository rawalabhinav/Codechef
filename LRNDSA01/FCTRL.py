def Z(n) :
	a,digits,i = n,0,1	
	while True :
		a = n//(5**i)
		digits += a
		if a == 0 :
			break
		else :
			i += 1
	return digits
arr = []
t = int(input())
for i in range(t) :
	arr.append(int(input()))
for n in arr:
	print(Z(n))
