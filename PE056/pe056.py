
def quersumm(number):
    summ = 0
    while number:
        summ += number%10
    
        number //= 10
    return summ
maxi = 0
for i in range(50, 100):
    for j in range(50, 100):
        new = quersumm(i**j)
        if new > maxi:
            maxi = new
print(maxi)
