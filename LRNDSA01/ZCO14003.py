n = int(input())
arr,brr = [],[]
for i in range(n) :
	arr.append(int(input()))
arr.sort(reverse = True)
for i in range(1,len(arr) +1) :
	brr.append(arr[i-1]*i )
print(max(brr))