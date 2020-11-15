## Hamming distance 

def ham(s1,s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count +=1
    return count



s1 = "CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG"
s2 = "ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT"





print(ham(s1,s2))


