import math
cprims=[]
inp=""
f = open("prims below one million.txt","r")
for line in f:
    inp+=line
prims=inp.split()
print("read")
for i in prims:
    si=str(i)
    if len(si)==1:
        cprims.append(i)
    else:
        cprim=1
        for j in range(1,len(si)+1):
            if not si[j:len(si)]+si[0:j] in prims:
                cprim=0
                break
        if cprim==1:
            cprims.append(i)
print(cprims)
count=1
for a in cprims:
    count+=1
print(count)
