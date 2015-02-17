mon=0
count=1
for a in range(0,3):
    for b in range(0,5):
        for c in range(0,11):
            for d in range(0,21):
                for e in range(0,41):
                   for f in range(0,101):
                       mon=a*100+b*50+c*20+d*10+e*5+f*2
                       if mon<201:
                           count+=1
print(count)
