for i in range(int(input())) :
	profit = []
	for j in range(int(input())) :
		s,v,p = map(int,input().split())
		profit.append((p//(s+1))*v)
	print(max(profit))