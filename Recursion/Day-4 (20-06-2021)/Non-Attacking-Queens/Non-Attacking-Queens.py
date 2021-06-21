class Solution:
    def solveNQueens(self, n):
        self.ans = []
        
        arr = [[0 for _ in range(n)] for _ in range(n)]
        
        self.helper(arr,0,n)
        return len(self.ans)
        
        
    def helper(self,arr,x,n):
        if x>=n:
            a = []
            for i in arr:
                a.append("".join(["." if x==0 else "Q" for x in i]))
            self.ans.append(a)
            return None
        
        for col in range(n):
            
            # initially in the (0,0) position
            if self.isSafe(arr,x,col,n):
                arr[x][col] = 1
                
                if self.helper(arr,x+1,n):
                    return True
            
                arr[x][col]=0
        return False
    
    def isSafe(self,arr,x,y,n):
        
        #Check if there is a queen in the same col above the given pos
        for i in range(x):
            if arr[i][y]==1:
                return False
        
        #Check the left upper diagonal
        row = x
        col = y
        
        while row>=0 and col>=0:
            
            if arr[row][col]==1:
                return False
            
            row-=1
            col-=1
            
        #Check the right upper diagonal
        row = x
        col = y
        
        while row>=0 and col<n:
            if arr[row][col]==1:
                return False
            
            row-=1
            col+=1
        
        return True
        
s = Solution()
n = int(input())
ans = s.solveNQueens(n)
if ans>0:
    print("There are",ans,"ways")
    print("Ways")
    print("----------------------------")
    for i in s.ans:
        for j in i:
            print(j)
        print("----------------------------")
else:
    print("Not Possible")

            
