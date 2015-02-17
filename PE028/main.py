nmbrs=[]
num=1
add=2
nmbrs.append(1)
while num<=(1001*1001):
    for i in range(0,4):
        num+=add
        nmbrs.append(num)
    add+=2
summ=0
for i in nmbrs:
    if i<=(1001*1001):
        summ+=i
print(summ)
        
