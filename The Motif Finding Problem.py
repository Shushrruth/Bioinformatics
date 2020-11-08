# Motif Finding Problem: Given a collection of strings, find a set of k-mers, one from each string, that minimizes the score of the resulting motif.

# Input: A collection of strings Dna and an integer k.
# Output: A collection Motifs of k-mers, one from each string in Dna, minimizing Score(Motifs) among all possible choices of k-mers.



from itertools import product

def Freak(genome,k):
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
    for x in lst:
        
        counter[x]=[]
        for gene in genome:
            mini=float('inf')
            for j in range(len(gene)-k+1):
                z = ham(x,gene[j:j+k])
                mini=min(mini,z)
            
            counter[x].append(mini)
                
              
    for s in counter:
        counter[s]= sum(counter[s])
    
    inv_map = {}
    for k, v in counter.items():
        inv_map[v] = inv_map.get(v, [])
        inv_map[v].append(k)
        
    return inv_map[min(inv_map)]

gene = ["TACATATCTACTAGCAGACAATCGAGCTATGATCTTGGTAAT",
        "ATCGACTCAAGCAATCTAGTGATGCATACTACGACTTCCATA",
        "GCGGATTGCATACATGCTACTACATCGCGAGTCGTGGGCAAC",
        "TTCCTTCTTATATGCATATATATTTGGCACTGCATGGGGACG",
        "TCCATAACTTTAGCAGGCGCCGTGCAACTCGATAGGGCTTTG",
        "TCGGGACAATCGTCGCTGAAATGACTTGTATGCCTGTCCATA",
        "ACGGGCGACTTGTAGAAATCCATATGCCGCTTCAGCCTGCGC",
        "TACATAGTCCTTGGATCTACCTTCTTAGGTCGTGTGGATCTG",
        "ACGGCCGGAGGATTCATACACTCTGACTAAGCGCAGGCCCGC",
        "ACTTGCACTGTGGTGGATAGGTCGTGCATACTTTTTAGTGAT"]

g = ["CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC",
     "GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC",
     "GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG"]

print(Freak(g,7))       