def getStatistics(numbers):
    ans = {}

    # Mean: sum of all the numbers divided by the total number of elments
    _sum = 0
    for i in numbers:
        _sum+=i

    ans["mean"] = _sum/len(numbers)

    # Median: Sort the numbers and find the middle element: if the length is odd then there is a single median else take the avg of the two elements
    nums = sorted(numbers)
    if len(nums)&1:
        #Odd
        index = len(nums)//2
        ans["median"] = nums[index]
    else:
        index1 = len(nums)//2
        index2 = index1-1
        median = (nums[index1]+nums[index2])/2
        ans["median"] = median

    # Mode
    myMap = {}
    for i in numbers:
        myMap[i] = myMap.get(i,0)+1
    
    _max = 0
    mode = None
    for i in myMap:
        if myMap[i]>_max:
            _max = myMap[i]
            mode = i
    
    ans["mode"] = mode

    # Sample variance
    '''
        The variance of a sample is the sum of the squared differences between each element and the mean of the elements. 
        Each term in the sum is divided by the number of input elements minus 1.

    '''

    _sum = 0
    mean = ans["mean"]
    for i in numbers:
        diff = i-mean
        squared = diff**2
        _sum = _sum + squared
    
    sampleVariance = _sum/(len(numbers)-1)

    ans["sample_variance"] = sampleVariance

    # Sample standard deviation: It is the square root of the sample variance.
    ans["sample_standard_deviation"] = sampleVariance**(0.5)

    # 95% confidence interval for the mean

    z_score = 1.96
    standardError = ans["sample_standard_deviation"]/(len(numbers)**(0.5))
    interval = [ans["mean"]-(z_score*standardError),ans["mean"]+(z_score*standardError)]

    ans["mean_confidence_interval"] = interval

    return ans

numbers = [int(x) for x in input().split()]
print(getStatistics(numbers))