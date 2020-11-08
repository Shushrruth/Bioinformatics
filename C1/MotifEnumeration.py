# Code Challenge: Implement MotifEnumeration (reproduced below).

# Input: Integers k and d, followed by a collection of strings Dna.
# Output: All (k, d)-motifs in Dna.





from itertools import product

def motif(DNA,k,t):
    rep = list(product('ATGC',repeat=k))
    lst = []
    for i in range(len(rep)):
        x = rep[i]
        char = ''
        for y in x:
            char = char + y
        lst.append(char)
        
    def ham(s1,s2):
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count +=1
        return count
    
    counter = {}
    for h in range(len(lst)):
        for i in range(len(DNA)):
            for j in range(len(DNA[i])-k+1):
                    if ham(lst[h],DNA[i][j:j+k]) <=t:
                        if lst[h] not in counter:
                            counter[lst[h]] = str(i)
                        else:
                            counter[lst[h]] = counter[lst[h]] + str(i)
                    
    return counter 




x = ["ATTTGGC","TGCCTTA","CGGTATC","GAAAATT"]
                    
print(motif(x,3,1))
                    
    




 
        
    
        