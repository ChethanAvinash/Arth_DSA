def interleavingStrings(one,two,three):
    # length of the third string must be the sum of the first and second strings.
    # if not the interleaving is not possible
    
    if len(three)!=len(two)+len(one):
        print("Yes")
        return False
    # 0,0 indicate the current positions of the pointer in the first string and
    # the second string.
    return helper(one,two,three,0,0)

def helper(one,two,three,i,j):
    
    # the position of in the third string is the sum of i and j indices.
    
    k = i+j # position of the pointer in the third string.
    # initially its value is 0
    
    # first we check if the first char of the first string is the same as the one of the third string. If yes we increment the i value to check the next char
    
    if k==len(three):
        return True
    
    if i<len(one) and one[i]==three[k]:
        if helper(one,two,three,i+1,j):
            return True
        
    # then we check the first char of the second string.
    
    if j<len(two) and two[j]==three[k]:
        if helper(one,two,three,i,j+1):
            return True
    return False
    
one = "algoexpert"
two = "your-dream-job"
three = "your-algodream-expertjob"
print(interleavingStrings(one,two,three))
