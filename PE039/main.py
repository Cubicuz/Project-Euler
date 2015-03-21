import math
pmax=0
imax=0
b=0
c=0
for p in range(3,1001):
    i=0
    for a in range(1,int(p/2)):
        c=(p*p-2*p*a+2*a*a)/(2*(p-a))
        if c%1 ==0:
            b=math.sqrt(c*c-a*a)
            if b%1 ==0:
                i+=1
    if i>imax:
        imax=i
        pmax=p
print(pmax)
                
