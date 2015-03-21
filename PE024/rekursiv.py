import copy
liste=[0,1,2,3,4,5,6,7,8,9]
perms=[]
def string(lis):
    text=""
    for k in lis:
        text+=str(k)
    return text
def swap(x,y,lis):
    save=lis[x]
    lis[x]=lis[y]
    lis[y]=save

def rek(j,lis):
    if j<9:
        zwlist=copy.deepcopy(lis)
        rek(j+1,zwlist)
        for k in range(j,9):
            zwlist=copy.deepcopy(lis)
            swap(j,k+1,zwlist)
            perms.append(string(zwlist))
            rek(j+1,zwlist)

liste=[0,1,2,3,4,5,6,7,8,9]
rek(6,liste)
print(perms)
