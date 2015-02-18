#a ist Multiplier, b ist Multiplicant
import math
numbrs=[]
numbr=1000
while numbr<100000:
    if '0' not in str(numbr):
        for a in range(1,int(math.sqrt(numbr))+1):
            b=numbr/a
            if (b%1)==0:
                nums= str(numbr)+str(a)+str(int(b))
                if len(nums)==9:
                    if '1' in nums:
                        if '2' in nums:
                            if '3' in nums:
                                if '4' in nums:
                                    if '5' in nums:
                                        if '6' in nums:
                                            if '7' in nums:
                                                if '8' in nums:
                                                    if '9' in nums:
                                                        if numbr not in numbrs:
                                                            numbrs.append(numbr)
                                                            print(numbr)
    numbr+=1
summ=0
for i in numbrs:
    summ+=i
print(summ)
