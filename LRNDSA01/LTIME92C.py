def check(string) :
    cnt = 0
    for i in string :
        if string[i+1] < string[i] :
            return False
        else :
            cnt += 1
    if cnt == len(string) :
        return True
def slices(s) :
    arr = []
    for j in range(len(s)):
        for i in range(len(s)) :
            a = s[i:j]
            if check(a) == True :
                arr.append(a)
    return arr
t = int(input())





'''t = int(input())
for i in range(t) :
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers = [x %2 for x in numbers]
    a = numbers.count(0)
    b = numbers.count(1)
    if b%2 == 0 :
        print(1)
    else :
        print(2)
'''


'''t = int(input())
for i in range(t) :
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers = [x %2 for x in numbers]
    if numbers.count(0) < numbers.count(1) :
        print(numbers.count(0))
    else :
        print(numbers.count(1))
'''

'''import math

def check(arr,k) :
    i = 0
    for x in arr :
        if x>k :
            return True
    if i == 0:
        return False
def compare(arr,k) :
    i = 0
    for x in arr :
        if x <= 1 and x != -1 :
            i += 1 
    if i == len(arr) :
        return True
    else :
        return False
t = int(input())
for i in range(t) :
    n,k = map(int,input().split())
    time = list(map(int, input().split()))
    if n - time.count(-1) < math.ceil(n/2) :
        print("Rejected")
    elif check(time,k) == True :
        print("Too Slow")
    elif compare(time,1) == True :
        print("Bot")
    else :
        print("Accepted")'''