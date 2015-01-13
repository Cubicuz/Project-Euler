#Memory Error
numbers = []
for i in range(0,100000000):
    numbers.append(0)
print("init done")
def rek(num):
    if num==1:
        pass
    else:
        #gerade
        if num%2==0:
            neu=int(num/2)
        #ungerade
        elif num%2==1:
            neu=3*num+1
        print(neu)
        if numbers[neu]==0:
            rek(neu)
        numbers[num]=numbers[neu]+1
        
for i in range(2,1000000):
    rek(i)
max=0
start=0
for i in range(0,1000000):
    if numbers[i]>max:
        max=numbers[i]
        start=i

print(start)
