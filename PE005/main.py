number=100000000
fin=0
while not fin:
    fin=1
    for i in range(11,21):
        if (number/i)%1!=0:
            fin=0
            break
    number+=20
print(number-20)

            
