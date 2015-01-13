inp = ""
with open('p067_triangle.txt') as f:
    for line in f:
        inp+=line
numbers = []
sub = inp.split()
for i in sub:
    numbers.append(int(i))
zeilen = 100
begin = 0
for i in range(0,zeilen):
    begin+=i
for i in range(zeilen-1,0,-1):
    for j in range(0,i):
        if(numbers[begin+j]>=numbers[begin+j+1]):
            numbers[begin-i+j] +=numbers[begin+j]
        else:
            numbers[begin-i+j] +=numbers[begin+j+1]
    begin-=i

print(numbers[0])
    




