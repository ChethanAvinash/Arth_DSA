# O(N) Time complexity and O(N) Space complexity where N is the length of the string.
def reverseWords(s):
    # These pointers are used to identify a word in the given string.
    startOfWord = 0
    endOfWord = 0
    ans = []

    while endOfWord<len(s):
        # if the current char is a space then we found a word 
        if s[endOfWord]==" ":
            wordEnd = endOfWord
            spaceStart = endOfWord
            while endOfWord<len(s) and s[endOfWord]==" ":
                endOfWord+=1
            
            ans.append(s[spaceStart:endOfWord]+s[startOfWord:wordEnd])            
            startOfWord = endOfWord

        endOfWord+=1

    ans.append(s[startOfWord:endOfWord])
    return "".join(ans[::-1])

s = "Demo is          the    best!"

print(reverseWords(s))