# O(n) TC and O(2n) where n is the length of the input string.
def runLengthEncoding(s):
    ans = []
    i = 0
    while i < len(s):
        count = 1
        
        j = i+1
        
        while j < len(s) and count<10 and s[i]==s[j]:
            j+=1
            count+=1
        
        ans.append(str(count))
        ans.append(s[i])
        i=j
    return "".join(ans)
    
s = "AAAAAABBBBBBDDDDDDAAAACC"
print(runLengthEncoding(s))