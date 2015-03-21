decpali=[]
for i in range(1,1000000):
    stringa=str(i)
    stringb=""
    for a in stringa:
        stringb=a+stringb
    if int(stringb)==i:
        decpali.append(i)

pali=[]
for j in decpali:
    i = j
    a = ""
    b = ""
    while i:
        if i & 1 == 1:
            a = "1" + a
            b = b + "1"
        else:
            a = "0" + a
            b = b + "0"
        i >>= 1
    if int(a)==int(b):
        pali.append(j)
print(pali)
summ=0
for i in pali:
    summ+=i
print(summ)
