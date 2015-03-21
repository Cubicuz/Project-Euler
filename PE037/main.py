inp=""
f = open("prims below one million.txt","r")
prims=[]
for line in f:
    prims.extend(line.split())
print("done reading")
a="123"

trunc=[]
minprim={"2","3","5","7"}
for a in prims:
    if len(a)>1:
        bol = 1
        for i in range(1,len(a)):
            if not a[i:] in prims:
                bol = 0
                break
            if not a[0:i] in prims:
                bol = 0
                break
        if bol==1:
            trunc.append(a)
summ=0
for a in trunc:
    summ+=a
print(summ)
