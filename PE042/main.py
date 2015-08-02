import math
inp=""
f = open("p042_words.txt","r")
words=[]
for line in f:
    words.extend(line.split('","'))
triangleNumbers = []
for i in range(1,100):
    triangleNumbers.append(0.5 * i * (i+1))
total = 0
for word in words:
    wordcount = 0
    for letter in word:
        wordcount += ord(letter)-64
    if wordcount in triangleNumbers:
        total += 1
print(total)