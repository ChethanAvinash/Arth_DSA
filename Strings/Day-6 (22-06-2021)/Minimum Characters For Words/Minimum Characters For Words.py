def getCharacters(words):
    myMap = {}

    for word in words:
        wordCount = {}
        for i in word:
            wordCount[i] = wordCount.get(i,0)+1
        for i in wordCount:
            myMap[i] = max(myMap.get(i,0),wordCount[i])

    return [ k for k,v in myMap.items() for _ in range(v)]

words = ["this","that","did","deed","them!","a"]
print(getCharacters(words))