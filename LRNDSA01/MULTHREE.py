for i in range(int(input())):
    k,d0,d1 = map(int, input().split())
    sum = d0+d1
    if k > 2:
        sum = sum + sum%10 + 20*((k-3)//4)
        for j in range((k-3)%4):
            sum += sum%10 #simple brute force
    if sum%3 == 0: 
        print("YES")
    else:
        print("NO")