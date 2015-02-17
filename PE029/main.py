numbrs=[]
for a in range(2,101):
    for b in range(2,101):
        ab= a**b
        if ab not in numbrs:
            numbrs.append(ab)
print(len(numbrs))
