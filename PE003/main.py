factor=0
result=0.1
bigzahl=600851475143
primfaktoren=[]
while factor<10000:
    factor+=1
    result=bigzahl/factor
    if (result%1)==0:
        print(factor)
        primfaktoren.append(factor)
        bigzahl/=factor
        

