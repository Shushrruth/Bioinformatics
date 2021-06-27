## Count d 

def count(pattern,text,d):
    def ham(s1,s2):
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count +=1
        return count
    
    
    
    k = len(pattern)
    count = 0
    for i in range(len(text)-k+1):
        z = text[i:i+k]
        if ham(z,pattern) <=d:
            count +=1 
    return count



pattern = "AAA"

text = "TACGCATTACAAAGCACA"

print(count(pattern,text,1))


