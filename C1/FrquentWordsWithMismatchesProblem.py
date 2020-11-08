from itertools import product

def Freak(genome,k,t):
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
    for i in range(len(lst)):
        for j in range(len(genome)-k+1):
            if ham(lst[i],genome[j:j+k]) <=t:
                if lst[i] not in counter:
                    counter[lst[i]] = 1
                else:
                    counter[lst[i]] +=1
                    
    inv_map = {}
    for k, v in counter.items():
        inv_map[v] = inv_map.get(v, [])
        inv_map[v].append(k)
        
    return inv_map[max(inv_map)]








t = "AATTTCAATAATCTCATTCACACAATCTCATTCCTCAACACACACACACTTCACACCTCAACACACACCTCACTCACCGCCCGCCCGCCTCAAATACACACACCCGCCTCAAATCTCAAATAATAATTTCCTCAACACTTCAATTTCTTCTTCCTCACCGCACACCCGCCTCAAATACACACACAATTTCCTCACCGCTTCTTCACACAATCCGCCTCAACACACACCCGCCCGCAATCCGCCTCACTCACTCACCGCAATACACAATAATAATCCGCTTCCCGCACACCTCAAATCCGCACACACACACACTTCCCGCCTCAAATCCGCCCGCAATACACCCGCTTC"

print(Freak(t,5,3))
                    
                    
                
    











