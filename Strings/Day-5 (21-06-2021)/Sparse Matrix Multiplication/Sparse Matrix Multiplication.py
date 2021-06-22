def normalMultiplcation(a,b,res):
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                res[i][j]+=a[i][k]*b[k][j]

'''
If the matrices are sparse ( i.e most of the elements are zeros ) then the above method is performing unnecessarily computations whose results are always zero.

if any row of the A matrix contains only zeros then the ans is always zero, this is the case with the columns in the B matrix.

So, before performing the multiplication, it is important to first identify the A matrix rows which contain only zeros and also the B matrix columns which contain only zeros.

In this way the number of computations can be reduced drastically.

'''

def sparseMatrixMultiplication(a,b,res):
    rowsA = [False]*len(a)
    colsB = [False]*len(b[0])

    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]!=0:
                rowsA[i] = True
                break
    
    for i in range(len(b[0])):
        for j in range(len(b)):
            if b[i][j]!=0:
                colsB[j] = True
                break
    

    for i in range(len(a)):
        for j in range(len(b[0])):
            if not rowsA[i] or not colsB[j]:
                res[i][j] = 0
                continue
                
            for k in range(len(b)):
                res[i][j]+=a[i][k]*b[k][j]
    
a = [
    [1,0,0],
    [-1,0,3]
]

b = [
    [7,0,0],
    [0,0,0],
    [0,0,1]
]

res = [
    [0,0,0],
    [0,0,0]
]

normalMultiplcation(a,b,res)
print(res)

res = [
    [0,0,0],
    [0,0,0]
]
sparseMatrixMultiplication(a,b,res)
print(res)






