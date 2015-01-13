numbera=999
numberb=999
palindrom=10
stringa=str(palindrom)
stringb=""
i=0
palindroems=[]
for i in stringa:
    stringb= i + stringb
while numberb>100:
    palindrom=numbera*numberb
    stringa=str(palindrom)
    stringb=""
    i=0
    for i in stringa:
        stringb= i + stringb
    if int(stringb)==palindrom:
        palindroems.append(palindrom)
    numbera-=1
    if numbera<100:
        numberb-=1
        numbera=999
palindroems.sort()
print(palindroems.pop())
