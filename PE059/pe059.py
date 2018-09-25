
inp=""
f = open("chipher.txt")
for line in f:
    inp+=line
strings = inp.split(",")
chars = []
for n in strings:
    chars.append(int(n))   

# after xor every char can be from 48 to 122 and the password is from 97 to 122

for i in range(0, len(chars), 3):
    
