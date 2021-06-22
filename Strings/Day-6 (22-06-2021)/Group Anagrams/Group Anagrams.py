def groupAnagrams(words):

    myMap = {}

    for word in words:
        key = "".join(sorted(word))
        if key not in myMap:
            myMap[key] = [word]
        else:
            myMap[key].append(word)
    
    print(list(myMap.values()))

words = ["yo","act","flop","tac","foo","cat","oy","olfp"]
groupAnagrams(words)