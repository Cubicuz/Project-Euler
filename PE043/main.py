pentagonal = []
maximum = 10000
for n in range(1,maximum+1):
	pentagonal.append(int(n*(3*n-1)/2))
print(pentagonal[9999])
for i in range(0,maximum-1):
	for j in range(i+1,maximum):
		summ = pentagonal[i] + pentagonal[j]
		summb = 0
		subb = pentagonal[j] - pentagonal[i]
		subbb = 0
		for n in range(j+1,maximum):
			if pentagonal[n] == summ:
				summb = 1
				for m in range(0,j):
					if pentagonal[m] == subb:
						print(subb)
						break
				break