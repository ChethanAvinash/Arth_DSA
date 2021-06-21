# O(n+m) is the time complexity and O(n) is the space complexity
# where n is the length of the chars string and m is the length of the doc string.
def generateDocument(chars,doc):
    myMap = {}

    for i in chars:
        myMap[i] = myMap.get(i,0)+1

    for i in doc:
        if i in myMap:
            if myMap[i]==1:
                myMap.pop(i)
            else:
                myMap[i]-=1
        else:
            return False

    return True

chars = "Bste!hetsi ogEAxpelrt x "
doc = "AlgoExpert is the Best!"
print(generateDocument(chars,doc))