import math
gsum=[]
for a in range(3,100000):
    summ=0
    for b in str(a):
        summ+=math.factorial(int(b))
    if a==summ:
        gsum.append(summ)
summ=0
for a in gsum:
    summ+=a
print(summ)
