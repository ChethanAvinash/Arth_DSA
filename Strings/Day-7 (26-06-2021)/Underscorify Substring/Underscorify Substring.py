def underscorify(s:str,sub):

    # Find all the occurences
    allOccurrences = []
    i = 0
    while i<len(s):
        foundIndex = s.find(sub,i)
        if foundIndex!=-1:
            allOccurrences.append([foundIndex,foundIndex+len(sub)])
            i = foundIndex+1
        else:
            i = i+1


    # Now we have to merge the overlapping occurrences
    prev = allOccurrences[0]
    merged = [prev]
    
    for j in range(1,len(allOccurrences)):
        curr = allOccurrences[j]

        if prev[1]>=curr[0]:
            prev[1] = curr[1]
        else:
            merged.append(curr)
            prev = curr

    # Now generate the new string
    ans = []
    stringIdx = 0
    locIdx = 0
    checkingIndex = 0
    isBetweenUnderscores = False

    while stringIdx<len(s) and locIdx<len(merged):
        
        if stringIdx==merged[locIdx][checkingIndex]:
            ans.append("_")
            isBetweenUnderscores = not isBetweenUnderscores
            if isBetweenUnderscores==False:
                locIdx+=1
            checkingIndex = 1 if checkingIndex==0 else 0

        ans.append(s[stringIdx])
        stringIdx+=1
    
    if stringIdx<len(s):
        ans.append(s[stringIdx:])
    
    print("".join(ans))
    

s = "testthis is a testtest to see if testestest it works"
sub = "test"
print(s)
underscorify(s,sub)