# Recursive Solution
def getAllValidIPAddresses(index,s,ans,allValidIps):
    #base case
    if len(ans)==4:
        # in some cases there may be 4 octets in the ans but some of the elements of s might still be unused.
        if index>=len(s):
            allValidIPs.append(".".join(ans))
        return

    '''
        We have to start from the given index and check 3 possibilities
        because every octet can have upto 3 digits ( 255 ) and a min of one digit ( 0 ).

    '''
    curr_octet = ""
    for i in range(index,index+3):
        # this condition checks for index out of range
        if i<len(s):
            curr_octet+=s[i]
            
            # an octet is invalid if it has a prefix 0 and a length greater than 1
            if curr_octet[0]=="0" and len(curr_octet)>1:
                break
                
            if 0<=int(curr_octet)<=255:
                ans.append(curr_octet)
                getAllValidIPAddresses(i+1,s,ans,allValidIps)
                ans.pop()
                # then we back track to find the next combinations by incrementing the index.

s = "1921680"
allValidIPs = []
getAllValidIPAddresses(0,s,[],allValidIPs)
print(allValidIPs)
            
        