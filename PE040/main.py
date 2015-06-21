stri=""
i =1
while len(stri)<1000000:
    stri+=str(i)
    i+=1
i=1
fac=1
while i<=1000000:
    print(stri[i-1])
    fac*=int(stri[i-1])
    i*=10
    
print(fac)
