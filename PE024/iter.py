p = []
perms=[]
for i in range(0,10):
    p.append(i)
counter=0
for a in p:
    perms.append(a)
    for b in p:
        if not b in perms:
            perms.append(b)
            for c in p:
                if not c in perms:
                    perms.append(c)
                    for d in p:
                        if not d in perms:
                            perms.append(d)
                            for e in p:
                                if not e in perms:
                                    perms.append(e)
                                    for f in p:
                                        if not f in perms:
                                            perms.append(f)
                                            for g in p:
                                                if not g in perms:
                                                    perms.append(g)
                                                    for h in p:
                                                        if not h in perms:
                                                            perms.append(h)
                                                            for i in p:
                                                                if not i in perms:
                                                                    perms.append(i)
                                                                    for j in p:
                                                                        if not j in perms:
                                                                            perms.append(j)
                                                                            counter+=1
                                                                            if counter==1000000:
                                                                                
                                                                                print(perms)
                                                                            del perms[-1]
                                                                        
                                                                    del perms[-1]
                                                                
                                                            del perms[-1]
                                                        
                                                    del perms[-1]
                                                
                                            del perms[-1]
                                        
                                    del perms[-1]
                                
                            del perms[-1]
                        
                    del perms[-1]
                
            del perms[-1]
        
    del perms[-1]
print("fin")

