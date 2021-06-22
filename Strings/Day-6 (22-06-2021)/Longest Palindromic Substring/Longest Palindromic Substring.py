def getLength(s,l,r):
    while l>=0 and r<len(s):
        if s[l]!=s[r]:
            break
        l-=1
        r+=1
    return [l+1,r]

def getLongestPalindromicSubstring(s):
    '''
        Palindromes can be of both even length and odd length
        eg: 

        racecar --> ODD length ( in this case we have center )
        aa --> even length ( here we don't )

        So to find the longest palindromic substring in the given string we must check all the even length substring and odd ones i.e every char must be treated in two ways 1] a part of an odd substring ( i.e by considering it to be the center )
             2] a part of an even substring 

    '''
    #since every char is a palindrome
    ans = [0,1] # starts at 0 and ends at zero

    for i in range(1,len(s)):
        #considering it to be a part of an even length palindromic substring
        even = getLength(s,i-1,i)
        
        #considering it to be a part of an odd length palindromic substring i.e it is considered as the center.
        odd = getLength(s,i-1,i+1)

        longest = max(odd,even,key=lambda x:x[1]-x[0])

        ans = max(ans,longest,key=lambda x:x[1]-x[0])


    return s[ans[0]:ans[1]]

s = "racecar"
print(getLongestPalindromicSubstring(s))


        

