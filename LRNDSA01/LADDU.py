a = "TOP_CONTRIBUTOR"
b = "CONTEST_HOSTED"
c = "CONTEST_WON"

t = int(input())
for i in range(t) :
	laddus = 0
	n,origin = input().split()
	for j in range(int(n)) :
		activity = input()
		if activity == a :
			laddus += 300
		elif activity == b:
			laddus += 50
		else :
			achievement,r = activity.split()
			if achievement == c :
				if int(r) < 20 :
					laddus += 320 - int(r)
				else :
					laddus += 300
			else :
				laddus += int(r)
	if origin == "INDIAN" :
		print(laddus//200)
	else :
		print(laddus//400)



