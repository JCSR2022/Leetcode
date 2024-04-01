class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        """       
        #aporach:
        #  dfs on board
        #     dfs on enconting a O
        #       Mark cels evaluated need a board on -1

        #2do aproach:
        # move thru the border dfs if find a 0

            check = [ [ -1 for _ in range(len(board[0]))] for _ in range(len(board))]
            # -1 Not check
            #  1 is a O already check not toching border or an X
            #  0 is a O already check toching border


        def makecheckBorder(i,j):
            if board[i][j] == 'X': check[i][j] = 1
            else: check[i][j] = 0
                
        def makecheck(i,j):
            if board[i][j] == 'X': 
                check[i][j] = 1
                return
      
            if  (check[i-1][j] == 0 or check[i+1][j] == 0 or 
                 check[i][j+1] == 0 or check[i][j-1] == 0):
                check[i][j] = 0
            else:
                check[i][j] = 1   
        
        top = 0
        bottom = len(board) - 1
        left = 0
        right = len(board[0]) -1
        
        #Top search:
        i = top
        for j in range(left,right+1):
            makecheckBorder(i,j)
        
        #bottom search:
        i = bottom
        for j in range(left,right+1):
            makecheckBorder(i,j)
        
        #right search:
        j = right
        for i in range(top,bottom+1):
            makecheckBorder(i,j)
        
        #left search:
        j = left
        for i in range(top,bottom+1):
            makecheckBorder(i,j)  
 
        while top <= bottom or left < right:
            top    +=1
            bottom -=1
            left   +=1
            right  -=1

            if top <= bottom:
                #Top search:
                i = top
                for j in range(left,right+1):
                    makecheck(i,j)
                #bottom search:
                i = bottom
                for j in range(left,right+1):
                    makecheck(i,j)
            if left < right:
                #right search:
                j = right
                for i in range(top,bottom+1):
                    makecheck(i,j)

                #left search:
                j = left
                for i in range(top,bottom+1):
                    makecheck(i,j) 

        for i in range(len(check)):
            for j in range(len(check[0])):
                if check[i][j] == 1:
                    board[i][j] = "X"
                else:
                    board[i][j] = "O"
        NO FUNCIONA NO SE POR QUE
        """       

        ROWS, COLS = len(board), len(board[0])
    
        
        def capture(r,c):
            if (r < 0  or c < 0  or 
                r == ROWS or c == COLS  or 
                board[r][c] != "O"):
                return
            board[r][c] = "T"
            
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)
        
    
        #1. Capture unsorranded regions  ( O -> T)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and 
                    (r in [0,ROWS-1]  or c in [0,COLS-1])) :
                    capture(r,c)
            
        #2. capture surroanded regions ( 0 -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        #3 uncapture (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"            
                    
                    
                    






















        
        
        
        