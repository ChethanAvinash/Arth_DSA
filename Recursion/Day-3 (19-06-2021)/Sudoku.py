def display(board):
    print()
    print("Solved:")
    for i in range(9):
        for j in range(9):
            print(board[i][j],end=" ")
        print()

def solveSudoku(board,i,j):
    if i==len(board):
        display(board)
        return 
        
    next_i = 0
    next_j = 0
    
    if j==(len(board[0])-1):
        next_i = i+1
        next_j = 0
    else:
        next_i = i
        next_j = j+1
    
    # if the current cell already has a value then we just move onto the next cell
    if board[i][j]!=0:
        solveSudoku(board,next_i,next_j)
    else:
        for num in range(1,10):
            # checking 1,2,3,4,5,6,7,8,9
            if isValid(board,i,j,num):
                # if the current is num is valid in the current cell then we put it and move onto the
                # next cell
                board[i][j] = num
                solveSudoku(board,next_i,next_j)
                # Then we have to remove the number updated just now incase the above call returns nothing
                # so that we can try a new num and check again.
                board[i][j] = 0
                
def isValid(board,row,col,num):
    
    # first check the complete row
    for j in range(9):
        if board[row][j]==num:
            return False
    
    # then check the complete column
    for i in range(9):
        if board[i][col]==num:
            return False
    
    # then we have to check its corresponding box
    # Every cell belongs to a box whose corner indices are given as
    
    start_i = 3*(row//3)
    start_j = 3*(col//3)
    
    for i in range(3):
        for j in range(3):
            if board[start_i+i][start_j+j]==num:
                return False
                
    return True
    
                
board = [[int(x) for x in input().split()] for _ in range(9)]
solveSudoku(board,0,0)