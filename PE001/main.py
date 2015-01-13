numberlist = []
i=0
for i in range(0,1000):
    numberlist.insert(i,0)
print(numberlist)
a=0
while a<1000:
    numberlist[a]=1
    a+=3
a=0
while a<1000:
    numberlist[a]=1
    a+=5
b=0
a=0
print(numberlist)
for i in range(0,1000):
   if numberlist[i]==1:
       b+=i
print(b)
