import math
triangle=0
divs=0
inc=0
#nicht bei 0 sondern bei einer hohen Zahl beginnen
while triangle<10000000:
    inc+=1
    triangle+=inc
while divs<500:
    inc+=1
    triangle+=inc
    divs=2
    obergrenze=int(math.sqrt(triangle))
    for i in range(2,obergrenze):
        if (triangle/i)%1==0:
            divs+=2
    if (triangle/obergrenze)%1==0:
        divs+=1
print(divs)
print(triangle)
