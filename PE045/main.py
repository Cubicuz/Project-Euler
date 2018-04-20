liste = []
for i in range(1,1000):
    liste.append(i*(3*i-1)/2)
print("listdone")
fin = 1
lowd=10000000
while fin==1:
    for a in range(0,999):
        for b in range(a+1,999):
            if liste[a]+liste[b] in liste:
                if liste[b]-liste[a] in liste:
                    if lowd<liste[b]-liste[a]:
                        lowd=liste[b]-liste[a]
                        print(lowd)
print(lowd)
    
            
    
