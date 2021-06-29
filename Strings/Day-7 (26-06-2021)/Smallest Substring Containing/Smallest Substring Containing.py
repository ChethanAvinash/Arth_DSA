def getSmallestSubstring(big,small):
    ans = ""
    myMap = {}
    for i in small:
        myMap[i] = myMap.get(i,0)+1
    
    i = -1
    j = -1

    count = 0
    desiredCount = len(small)
    bigMap = {}

    while True:

        f1 = False
        f2 = False

        while i<len(big)-1 and count<desiredCount:
            f1 = True
            i+=1
            bigMap[big[i]] = bigMap.get(big[i],0)+1

            if bigMap[big[i]]<=myMap.get(big[i],0):
                count+=1
        
        while j<i and count==desiredCount:
            f2 = False

            potentialAns = big[j+1:i+1]
            if len(ans)==0 or len(potentialAns)<len(ans):
                ans = potentialAns

            j+=1
            if bigMap[big[j]]==1:
                bigMap.pop(big[j])
            else:
                bigMap[big[j]]-=1
            
            if bigMap.get(big[j],0)<myMap.get(big[j],0):
                count-=1
        if not f1 and not f2:
            break
    return ans

bigString = input()
smallString = input()
print(getSmallestSubstring(bigString,smallString))