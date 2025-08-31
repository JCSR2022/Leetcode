class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        #aproach:
        # for each cell put all posible values if list ==1 cahnge and update


        def finPossible(x,y):
    
            if board[x][y] != '.':
                return {board[x][y]}
            
            #find square
            sq_i,sq_j = 3*(x//3),3*(y//3)
            elements = set()
            for i in range(sq_i,sq_i+3):
                for j in range(sq_j,sq_j+3):
                    if board[i][j] != '.':
                            elements.add(board[i][j])
                            
            #find colum
            for i in range(9):
                if board[i][y] != '.':
                    elements.add(board[i][y])
            
            #find row
            for j in range(9):
                if board[x][j] != '.':
                    elements.add(board[x][j])
                    
                    
            return {num for num in "123456789" if num not in elements}


        change = True
        while change :
            change = False
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        curr = finPossible(i,j)
                        if len(curr) == 1:
                            board[i][j] = curr.pop()
                            change = True

                



            