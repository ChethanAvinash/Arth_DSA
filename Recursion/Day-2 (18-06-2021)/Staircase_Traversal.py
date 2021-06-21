# Printing all the stair paths
def getWays(height,maxSteps,ans,count):
    if height<0:
        #If we go above the given height we have to just return ( no path )
        return
    elif height==0:
        # Then we have solution and we have to print it and update 
        # the count
        count[0]+=1
        print(ans[:-3])
        return

    # We check all the steps till the maxSteps
    for i in range(1,maxSteps+1):
        getWays(height-i,maxSteps,ans+str(i)+" ->",count)

height = int(input())
maxSteps = int(input())
count = [0]
print("The available ways: ")
getWays(height,maxSteps,"",count)
print("Total number of ways: ",count[0])


# We we just want the number of ways then dynamic programming must be
# used.

def getWaysDP(height,maxSteps):
    dp = [0]*(height+1)

    # Every element in the dp list indicates the number of ways to reach the final step from the corresponding height

    dp[height] = 1 
    
    #there is one way to reach the last step from the last step itself i.e we don't jump

    for i in range(height-1,-1,-1):
        for j in range(1,maxSteps+1):
            if i+j<len(dp):
                dp[i] = dp[i] + dp[i+j]

    return dp[0]

height = int(input())
maxSteps = int(input())
print("Total number of ways: ",getWaysDP(height,maxSteps))