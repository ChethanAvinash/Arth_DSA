'''
This is a classic example of a catalan number.

Eg: 2nd catalan number is given as

2nd = 1st*0th + 0th*1st

3rd = 2nd*0th + 1st*1st + 0th*2nd

For the number of the binary tree topologies given "n"

n = 3

Possible configurations are 5

  1          1         1        1        1
 / \        /         /          \        \ 
2   3      2         2            2        2
          /           \          /          \ 
         3             3        3            3

The count is the same as the 3rd catalan number.

'''

def getCount(n):
    if n==0 or n==1:
        return 1

    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2,n+1):
        for j in range(i):
            dp[i]+= dp[j]*dp[i-j-1]

    return dp[n]

n = int(input())
print(getCount(n))