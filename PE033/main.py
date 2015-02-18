aas=[]
bbs=[]
for a in range(0,99):
    for b in range(a+1,100):
        try:
            if ('1' in str(a))&('1' in str(b)):
                if (a/b)==(int(str(a).replace("1",""))/int(str(b).replace("1",""))):
                    aas.append(int(str(a).replace("1","")))
                    bbs.append(int(str(b).replace("1","")))
            if ('2' in str(a))&('2' in str(b)):
                if (a/b)==(int(str(a).replace("2",""))/int(str(b).replace("2",""))):
                    aas.append(int(str(a).replace("2","")))
                    bbs.append(int(str(b).replace("2","")))
            if ('3' in str(a))&('3' in str(b)):
                if (a/b)==(int(str(a).replace("3",""))/int(str(b).replace("3",""))):
                    aas.append(int(str(a).replace("3","")))
                    bbs.append(int(str(b).replace("3","")))
            if ('4' in str(a))&('4' in str(b)):
                if (a/b)==(int(str(a).replace("4",""))/int(str(b).replace("4",""))):
                    aas.append(int(str(a).replace("4","")))
                    bbs.append(int(str(b).replace("4","")))
            if ('5' in str(a))&('5' in str(b)):
                if (a/b)==(int(str(a).replace("5",""))/int(str(b).replace("5",""))):
                    aas.append(int(str(a).replace("5","")))
                    bbs.append(int(str(b).replace("5","")))
            if ('6' in str(a))&('6' in str(b)):
                if (a/b)==(int(str(a).replace("6",""))/int(str(b).replace("6",""))):
                    aas.append(int(str(a).replace("6","")))
                    bbs.append(int(str(b).replace("6","")))
            if ('7' in str(a))&('7' in str(b)):
                if (a/b)==(int(str(a).replace("7",""))/int(str(b).replace("7",""))):
                    aas.append(int(str(a).replace("7","")))
                    bbs.append(int(str(b).replace("7","")))
            if ('8' in str(a))&('8' in str(b)):
                if (a/b)==(int(str(a).replace("8",""))/int(str(b).replace("8",""))):
                    aas.append(int(str(a).replace("8","")))
                    bbs.append(int(str(b).replace("8","")))
            if ('9' in str(a))&('9' in str(b)):
                if (a/b)==(int(str(a).replace("9",""))/int(str(b).replace("9",""))):
                    aas.append(int(str(a).replace("9","")))
                    bbs.append(int(str(b).replace("9","")))
        except:
            i=0
i=1
for a in aas:
    i*=a
a=i
i=1
for b in bbs:
    i*=b
print(int(i/a))

