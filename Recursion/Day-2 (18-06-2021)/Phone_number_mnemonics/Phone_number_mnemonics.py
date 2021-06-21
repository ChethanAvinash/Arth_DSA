class Solution:
    def __init__(self):
        self.db = ["0","1","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

    def solve(self,phoneNo,ans):
        if len(phoneNo)==0:
            print(f"  \"{ans}\",")
            return

        first = phoneNo[0]
        rem = phoneNo[1:]

        current = self.db[ord(first)-ord("0")]

        for i in current:
            self.solve(rem,ans+i)

phoneNumber = input().strip()
s = Solution()
print("[")
s.solve(phoneNumber,"")
print("]")