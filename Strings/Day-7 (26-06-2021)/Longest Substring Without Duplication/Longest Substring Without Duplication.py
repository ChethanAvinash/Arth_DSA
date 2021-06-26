def longestSubstring(s):
    i = -1
    j = -1
    ans = [0,""]
    myMap = {}
    while True:
        
        f1 = False
        f2 = False

        while i<len(s)-1:
            f1 = True
            i+=1
            myMap[s[i]] = myMap.get(s[i],0)+1

            if myMap[s[i]]==2:
                break
            else:
                if i-j > ans[0]:
                    ans[0] = i-j
                    ans[1] = s[j+1:i+1]

        while j<i:
            f2 = True
            j+=1
            myMap[s[j]] = myMap[s[j]] -1
            if myMap[s[j]]==1:
                if i-j > ans[0]:
                    ans[0] = i-j
                    ans[1] = s[j+1:i+1]
                break

        if not f1 and not f2:
            break

    return ans

s = "clementisacap"
print(longestSubstring(s))
        

            
