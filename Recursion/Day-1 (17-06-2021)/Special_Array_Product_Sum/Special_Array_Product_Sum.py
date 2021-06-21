def getProductSum(arr,d):
    _sum = 0
    for i in arr:
        if type(i) is list:
            _sum = _sum + getProductSum(i,d+1)
        else:
            _sum = _sum + i
    return _sum*d

arr = [1,[1,[-1]]]
print(getProductSum(arr,1))