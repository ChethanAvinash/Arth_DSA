def getCipher(s,k):
    '''
        K can be any large number but whatever may be its value it keeps cycling
        as we are dealing with only the lowercase alphabets ( 26 )

        SO we can modify K to be K%26 ( if k > 26 then the remainder ensures the result is between 1 and 25)

        in Python ord() function returns the ASCII value of any character. Without using this method we could also store all the ASCII values of "a" to "z" in a hashMap and use them for the conversion.

        and chr() is the method that returns a char for the given ASCII value 

    '''
    k = k%26
    ans = []
    for char in s:
        new_ASCII = ord(char) + k
        if new_ASCII>122:
            # Since 122 is the ASCII value of "z"
            ans.append(chr(96 + new_ASCII%122))
        else:
            ans.append(chr(new_ASCII))
    
    return "".join(ans)

s = input("Enter the string: ").strip()
k = int(input())
print(getCipher(s,k))