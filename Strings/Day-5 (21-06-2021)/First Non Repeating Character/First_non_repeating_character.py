# Brute force
# For every char we traverse the remaining portion of the string to check for its next occurrence
# O(n^2) TC and O(1) Space
def find(s):
    for i in range(len(s)):
        found = False
        for j in range(len(s)):
            if s[i]==s[j] and i!=j:
                found = True
        if not found:
            return i
    return -1

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

