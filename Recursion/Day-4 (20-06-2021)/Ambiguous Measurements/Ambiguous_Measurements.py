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