maxprims=0
maxa=0
maxb=0

for a in range(-1000,1000):
    print(a)
    for b in range(-1000,1000):
        bol=0
        prims=0
        inc=0
        while bol==0:
            num=inc*inc+a*inc+b
            for i in range(2,int(num/2)):
                if (num/i)%1==0:
                    bol=1
            inc+=1
        inc-=1
        if maxprims<inc:
            maxprims=inc
            maxa=a
            maxb=b
print(maxa,maxb,maxa*maxb)
