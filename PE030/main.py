summ=0
numbr=2
tmp=0
tmps=""
while numbr<1000*1000:
    tmp=0
    tmps=str(numbr)
    for i in tmps:
        tmp+=int(i)**5
    if tmp==numbr:
        summ+=numbr
    numbr+=1
print(summ)
