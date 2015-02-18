import math
prims=[]
for i in range(1,1000000):
    prim=1
    for j in range(2,int(math.sqrt(i))+1):
        if (i/j)%1==0:
            prim=0
            break
    if prim==1:
        prims.append(str(i))
f = open("prims below one million.txt",'w')
f.write(" ".join(prims))
f.close()
