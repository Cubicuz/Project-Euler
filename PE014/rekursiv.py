#Memory Error
cache=dict()
print("init done")
maxstartnumber = 0
maxstartcount = 0
cache[1] = 0

def rek(num):
    global maxstartcount
    global maxstartnumber
    if num!=1:
        #ungerade
        if num & 1:
            neu=3*num+1
        #gerade
        else:
            neu=int(num/2)
#        print(neu)
        if not neu in cache:
            rek(neu)
        cache[num]=cache[neu]+1
        if cache[num] > maxstartcount:
            maxstartnumber = num
            maxstartcount = cache[num]

def rek1(num):
    global maxstartcount
    global maxstartnumber
    if num in cache:
        return cache[num]+1
    if num & 1:
        neu=3*num + 1
    else:
        neu=int(num/2)
    cache[num]=rek1(neu)+1
    if cache[num] > maxstartcount:
        maxstartcount = cache[num]
        maxstartnumber = num
        

for i in range(2,1000000):
    rek(i)
print("Maxstartnumber: " + str(maxstartnumber))
print("Maxstartcount: " + str(maxstartcount))
