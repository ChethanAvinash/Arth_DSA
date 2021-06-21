def getPermutations(s,ans,arr):
    if len(s)==0:
        arr.append(ans.split()[1:])
        return

    for i in range(len(s)):
        current = s[i]
        getPermutations(s[:i]+s[i+1:],ans+" "+current,arr)
    
s = input().strip()
arr = []
getPermutations(s,"",arr)
print(arr)

