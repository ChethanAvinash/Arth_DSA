# Brute force
# For every char we traverse the remaining portion of the string to check for its next occurrence
# O(n^2) TC and O(1) Space
def find(s):
    found_index = -1
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if s[i]==s[j]:
                break
        else:
            found_index=i
            break
    return found_index

s = "abbdcaf"
print(find(s))

# Using a hashMap
# O(n) TC and O(26) SC because there are only 26 letters
def findNonRepeating(s):

    myMap = {}
    for i,val in enumerate(s):
        if val not in myMap:
            myMap[val] = [[val,i]]
        else:
            myMap[val].append([val,i])
        
    for i in myMap:
        if len(myMap[i])==1:
            return myMap[i][0][1]

s = "abbdcaf"
print(findNonRepeating(s))

