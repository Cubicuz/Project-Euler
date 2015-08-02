import math
prims=[2,3]
for i in range(5,1000000):
    prim=1
    maxRange = math.sqrt(i)+1
    for j in prims:
        if j >= maxRange:
            break
        if (i%j)==0:
            prim=0
            break
    if prim==1:
        prims.append(i)
print("done")
#f = open("prims below one million.txt",'w')
#f.write(" ".join(prims))
#f.close()
