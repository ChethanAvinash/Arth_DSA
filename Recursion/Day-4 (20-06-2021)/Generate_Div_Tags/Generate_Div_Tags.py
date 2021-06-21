def generateDivTags(opening_div,closing_div,ans):
    if opening_div==0 and closing_div==0:
        print(ans)
        return

    if opening_div!=0:
        generateDivTags(opening_div-1,closing_div,ans+"<div>")
    
    if closing_div>opening_div:
        generateDivTags(opening_div,closing_div-1,ans+"</div>")

numberOfTags = int(input())
generateDivTags(numberOfTags,numberOfTags,"")
