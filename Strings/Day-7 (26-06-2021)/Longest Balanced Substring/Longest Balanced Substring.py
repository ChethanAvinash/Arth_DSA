# O(n) TC and O(n) SC
def getLongestBalancedSubstring(s):

    char_Stack = []
    index_Stack = [-1]
    ans = float("-inf")

    for i,val in enumerate(s):
        if val=="(":
            char_Stack.append(val)
            index_Stack.append(i)
        else:
            # check if there exists an opening bracket before
            if len(char_Stack)!=0 and char_Stack[-1]=="(":
                char_Stack.pop()
                index_Stack.pop()

                # Now we have a potential answer
                ans = max(ans,i-index_Stack[-1])
            else:
                index_Stack.append(i)
            
    return ans

# O(N) TC and O(1) SC 
def spaceOptimized(s):
    # We perform two passes 1] Left to right and 2] Right and Left and find the max length

    left = 0
    right = 0
    ans = float("-inf")

    for i in range(len(s)):
        if s[i]=="(":
            left+=1
        elif s[i]==")":
            right+=1
        
        if right==left:
            # Then we have found a balanced substring
            ans = max(ans,right*2)
        elif right>left:
            left = 0
            right = 0
    
    # Right pass
    left = 0
    right = 0
    for i in range(len(s)-1,-1,-1):
        if s[i]=="(":
            left+=1
        elif s[i]==")":
            right+=1
        
        if right==left:
            ans = max(ans,right*2)
        elif left > right:
            left = 0
            right = 0
    
    return ans

s = input()
print(getLongestBalancedSubstring(s))
print(spaceOptimized(s))