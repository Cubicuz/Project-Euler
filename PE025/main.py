f1=1
f2=1
f3=2
i=3
while len(str(f3))<1000:
    i+=1
    f1=f2
    f2=f3
    f3=f1+f2
print(i)
