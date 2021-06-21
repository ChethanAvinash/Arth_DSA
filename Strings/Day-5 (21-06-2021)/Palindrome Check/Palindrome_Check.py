# Approach-1
# Two pointer technique O(n) TC and O(1) SC where n is the length of the string
def palindromeCheck(s):
    l = 0
    r = len(s)-1

    while l<r:
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1

    return True

print(palindromeCheck("racecar"))

# Approach-2
# Just compare the string and the reverse of the string ( O(n) TC )
s = "racecar"
print(s==s[::-1])
