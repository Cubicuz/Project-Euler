#A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
#    1/2	= 	0.5
#    1/3	= 	0.(3)
#    1/4	= 	0.25
#    1/5	= 	0.2
#    1/6	= 	0.1(6)
#    1/7	= 	0.(142857)
#    1/8	= 	0.125
#    1/9	= 	0.(1)
#    1/10	= 	0.1 
#
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

#vorgehensweise: schriftliches dividieren, der Rest kommt in ein Dict(), bzw wird überprüft ob er schon drinn ist

#beginne bei d=999 für eventuelle optimierung


d=999
longestRecurringCycle = 0
longestRecurringId = 0
while d>(longestRecurringCycle+1):
    restToFirstAppearing = []
    numbr = 1   # linke zahl beim schriftlichen dividieren
    cont = 1    # continue variable
    currentPos = 0
    while cont==1:
        rest = numbr%d
        if rest == 0:    # sauberes Ende der Division, kein recurring cycle
            cont = 0
        else :
            if rest in restToFirstAppearing:    # recurring cycle gefunden
                cont = 0
                ind = restToFirstAppearing.index(rest)
                recurringCycle = currentPos - ind
                #print(recurringCycle)
                if recurringCycle > longestRecurringCycle:
                    longestRecurringCycle = recurringCycle
                    longestRecurringId = d
            else:
                restToFirstAppearing.append(rest)
                currentPos +=1
            
        numbr = rest * 10         #nächster Schritt beginnt mit rest*10
        
    d-=1
print(longestRecurringCycle)
print(longestRecurringId)
