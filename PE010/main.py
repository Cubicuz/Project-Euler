from math import sqrt

numbers = []
numbers.append(2)
numbers.append(3)
zahl=3
prim=0
while zahl<2000000:
    zahl+=2
    prim=1
    for x in numbers:
        if x > zahl/3:
            break
        if (zahl/x)%1==0:
            prim=0
            break
    if prim==1:
        numbers.append(zahl)
        print(zahl)
summe=0
for a in numbers:
    summe+=a
print(summe)
