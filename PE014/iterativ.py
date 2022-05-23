#!/bin/python3

cache=dict()

maxseq=0
maxstart=0
for i in range(2,1_000_000):
    curseq=0
    curnumb=i
    while curnumb>1:
        curseq+=1
        if curnumb%2==0:
            curnumb/=2
        else:
            curnumb=3*curnumb+1
    if curseq>maxseq:
        maxstart=i
        maxseq=curseq
print(maxstart)
