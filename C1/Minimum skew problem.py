##  All integer(s) i minimizing Skew  (Genome)

def count(text):
    for i in range(len(text)+1):
        G = 0
        C = 0
        counter = []
        y = text[:i]
        for j in y:
            if j == "G":
                G +=1
            if j =="C":
                C += 1
            counter.append(G-C)
            
    
    return counter 


x = count("GATACACTTCCCGAGTAGGTACTG")



