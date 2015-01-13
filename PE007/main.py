numbers = []
numbers.append(2)
numbers.append(3)
i = 2
zahl=3
prim=0
while i<10001:
    zahl+=2
    prim=1
    for x in numbers:
        if (zahl/x)%1==0:
            prim=0
            break
    if prim==1:
        i+=1
        numbers.append(zahl)
        print(str(i) + ": " + str(zahl))
print(numbers.pop())
