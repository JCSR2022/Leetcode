class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        ref = list(range(1,10))

        def transformBoard():
            for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j].isnumeric():
                        board[i][j] = int(board[i][j])
                    else:
                        board[i][j] = None

        def check_subBox(i,j):
            vector = []
            for n in range(i,i+3):
                for m in range(j,j+3):
                    vector.append(board[n][m])
            vector = [elem for elem in vector if elem is not None]
            return check_digits_1_9(vector) and check_without_repetition(vector)

        def check_row(i):
            vector = [elem for elem in board[i] if elem is not None]  
            return check_digits_1_9(vector) and check_without_repetition(vector)

        def check_column(j):
            vector = []
            for i in range(len(board)):
                if board[i][j]:
                    vector.append(board[i][j])
            return check_digits_1_9(vector) and check_without_repetition(vector)

        def check_digits_1_9(vector):
            return  vector == [val for val in vector if val in ref ]

        def check_without_repetition(vector):
            return len(set(vector)) == len(vector)


        def globalCheck():
            for i in range(0,len(board),3):
                for j in range(0,len(board),3):
                    if not check_subBox(i,j): return False

            for i in range(0,len(board)):
                if not check_row(i): return False

            for j in range(0,len(board)):
                if not check_column(j): return False

            return True
        
        transformBoard()
        return globalCheck()
        
    
            
        
        