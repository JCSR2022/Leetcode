class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def countNeighbors(i,j):
            def upLimit(x):
                return max(x,0)
            def dowLimit(x):
                return min(x,len(board))
            def leftLimit(x):
                return max(x,0)
            def rightLimit(x):
                return min(x,len(board[0]))

            count = 0
            for k in range(upLimit(i-1),dowLimit(i+2)):
                count += sum(board[k][leftLimit(j-1):rightLimit(j+2)])
            count -= board[i][j]
            return count

        newboard = [[0]*len(board[0]) for _ in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                cellNeighborcount = countNeighbors(i,j)
                #print("pos:",(i,j),cellNeighborcount)
                
                if cellNeighborcount < 2:
                    newboard[i][j] = 0    
                elif cellNeighborcount > 3:
                    newboard[i][j] = 0
                elif cellNeighborcount == 3:
                    newboard[i][j] = 1
                else: #cellNeighborcount == 2
                    newboard[i][j] = board[i][j]
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = newboard[i][j]
                
              
            
            
                
            
            
        