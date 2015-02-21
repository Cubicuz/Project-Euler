amics = []
numbers=[]
summ=0
numbers.append(0)
for i in range(1,10000):
    summ=0
    for j in range(1,int((i)/2)+1):
        if ((i/j)%1==0):
            summ+=j
    numbers.append(summ)
for i in range(1,10000):
    summ=numbers[i]
    if (summ<10000):
        if numbers[summ]==i:
            if summ!=i:
                amics.append(i)
summ=0
for i in amics:
    summ+=i
print(amics)
print(summ)
