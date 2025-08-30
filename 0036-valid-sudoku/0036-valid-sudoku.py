class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        #change to nums

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    board[i][j] = int(board[i][j])
                else:
                    board[i][j] = 0

        #validate rows
        for i  in range(9):
            num_in_row =  set() 
            for j in range(9):
                if board[i][j] != 0:
                    if board[i][j] in num_in_row:
                        #print("row:",(i,j),board[i][j], num_in_row)
                        return False
                    num_in_row.add(board[i][j] )

        #validate cols
        for j in range(9):
            num_in_col = set()
            for i in range(9):
                if board[i][j] != 0:
                    if board[i][j] in num_in_col:
                        #print("col:",(i,j),board[i][j], num_in_col)
                        return False
                    num_in_col.add(board[i][j] )

        #validate squares
        for i,j in [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]:
            num_in_square = set()
            for idx in range(i,i+3):
                for jdx in range(j,j+3):
                    if  board[idx][jdx] != 0:
                        if board[idx][jdx] in num_in_square:
                            #print("square:",(idx,jdx),board[idx][jdx], num_in_square)
                            return False
                        num_in_square.add(board[idx][jdx])

        return True
 #---------------------------------------------------------------   
        # #validate row, col and 3x4 squares..

        # size = 9

        # #validate rows
        # for row in board:
        #     num_in_row = [ num for num in row if num != "." ]
        #     #print(num_in_row,len(set(num_in_row)) != len(num_in_row))
        #     if len(set(num_in_row)) != len(num_in_row):
        #         return False
        
        # #print()
        # #validate cols
        # for j in range(size):
        #     num_in_col = [ board[i][j] for i in range(size) if board[i][j] != "."]
        #     #print(num_in_col,len(set(num_in_col)) != len(num_in_col))
        #     if len(set(num_in_col)) != len(num_in_col):
        #         return False
        
        # #print()
        # #validate squares
        # for i,j in [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]:
        #     num_in_square = []
        #     for idx in range(i,i+3):
        #         for jdx in range(j,j+3):
        #             if  board[idx][jdx] != "." :
        #                 num_in_square.append(board[idx][jdx])
        #     #print(num_in_square,len(set(num_in_square)) != len(num_in_square))
        #     if len(set(num_in_square)) != len(num_in_square):
        #         return False

        # return True


































        # ref = list(range(1,10))

        # def transformBoard():
        #     for i in range(len(board)):
        #         for j in range(len(board)):
        #             if board[i][j].isnumeric():
        #                 board[i][j] = int(board[i][j])
        #             else:
        #                 board[i][j] = None
                        
        # def check_digits_1_9(vector):
        #     return  vector == [val for val in vector if val in ref ]

        # def check_without_repetition(vector):
        #     return len(set(vector)) == len(vector)                        
        

        # def check_subBox(i,j):
        #     vector = []
        #     for n in range(i,i+3):
        #         for m in range(j,j+3):
        #             vector.append(board[n][m])
        #     vector = [elem for elem in vector if elem is not None]
        #     return check_digits_1_9(vector) and check_without_repetition(vector)

        # def check_row(i):
        #     vector = [elem for elem in board[i] if elem is not None]  
        #     return check_digits_1_9(vector) and check_without_repetition(vector)

        # def check_column(j):
        #     vector = []
        #     for i in range(len(board)):
        #         if board[i][j]:
        #             vector.append(board[i][j])
        #     return check_digits_1_9(vector) and check_without_repetition(vector)




        # def globalCheck():
        #     for i in range(0,len(board),3):
        #         for j in range(0,len(board),3):
        #             if not check_subBox(i,j): return False

        #     for i in range(0,len(board)):
        #         if not check_row(i): return False

        #     for j in range(0,len(board)):
        #         if not check_column(j): return False

        #     return True
        
        # transformBoard()
        # return globalCheck()
        
    
            
        
        