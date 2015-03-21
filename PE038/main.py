


high = 0
for i in range(2,10000):
    a = ""
    cnt=1
    while len(a)<9:
        a+= str(cnt*i)
        cnt+=1
    if len(a)==9:
        if int(a)>high:
            if "1" in a:
                if "2" in a:
                    if "3" in a:
                        if "4" in a:
                            if "5" in a:
                                if "6" in a:
                                    if "7" in a:
                                        if "8" in a:
                                            if "9" in a:
                                                high=int(a)
print(high)
