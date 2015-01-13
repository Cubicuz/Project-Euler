#20 Horizontale und 20 Vertikale Wege sind insgesammt 40 wege
#20 Horizontale Wege können wir beliebig verteilen, die 20 Vertikalen sind abhängig
# ohne zurücklegen ohne reihenfolge: n! / (k! * (n-k)!) ich verwende allerdings ne PC Optimierte gleicheung
n=40
k=20
zaehler=1
nenner=1
for i in range(n-k+1,n+1):
    zaehler*=i
for i in range(1,k+1):
    nenner*=i
print(int(zaehler/nenner))
