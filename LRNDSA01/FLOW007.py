t = int(input())
a = []
for i in range(t):
	n = input()
	a.append(n[::-1])
for i in a :
	print(int(i))