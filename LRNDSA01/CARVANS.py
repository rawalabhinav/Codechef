t = int(input())
for i in range(t) :
	n = int(input())
	speed = [int(j) for j in input().split()]
	j = speed[0]
	cnt = 1
	for k in speed :
		if j > k :
			cnt += 1
			j = k
	print(cnt)
