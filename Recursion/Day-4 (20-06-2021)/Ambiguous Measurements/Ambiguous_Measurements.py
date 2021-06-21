def canMeasure(cups,n,lower,upper,res_lower,res_upper):
    if n<0:
        return False
    
    if res_lower>upper:
        return False
    
    if res_lower<=lower and res_lower<=upper and res_upper>=lower:
        return True
    
    include = canMeasure(cups,n,lower,upper,res_lower+cups[n][0],res_upper+cups[n][1])
    exclude = canMeasure(cups,n-1,lower,upper,res_lower,res_upper)
    
    return  include or exclude
    
cups = [[100,200],[450,465],[800,850]]
lower = 2100
upper = 2300
print(canMeasure(cups,len(cups)-1,lower,upper,0,0))

# Approach-2 ( with memoization )

def canMeasureDP(cups,lower,upper,dp):
    '''
        A list or a matrix can't be used for DP because the limits are unknown
        i.e we are given with only the ranges hence a fixed DP array is not
        possible. Therefore a hashmap is a good option to store all the 
        possible lower ans upper levels and a unique key is assigned that is 
        based on the lower and upper values itself.

    '''
    _key = str(lower) + ":" + str(upper)

    # if there is a value for the given key in the hashmap then we have to 
    # return the pre-computed value.

    if _key in dp:
        return dp[_key]
    
    if lower<=0 and upper<=0:
        # we have exceeded
        return False
    
    canMeasure = False
    for cup in cups:
        cupLow,cupHigh = cup
        if lower<=cupLow and cupHigh<=upper:
            canMeasure = True
            break
        newLow = max(0,lower-cupLow)
        newHigh = max(0,upper-cupHigh)
        canMeasure = canMeasureDP(cups,newLow,newHigh,dp)
        if canMeasure:
            break
    dp[_key] = canMeasure
    return canMeasure

    
cups = [[100,200],[450,465],[800,850]]
lower = 2100
upper = 2300
dp = {}
print(canMeasureDP(cups,lower,upper,dp))