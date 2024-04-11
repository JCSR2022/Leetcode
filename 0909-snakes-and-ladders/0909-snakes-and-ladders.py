class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        length = len(board)

        def intToPos(square):
 
            square = square -1

            r = square//length
            if r%2 == 0:
                c = square%length
            else:
                 c = length - square%length -1

            r = length - r -1

            return [r, c]

    
        q = deque()
        visit = set()
        q.append([1,0])
        
        while q:
            # print(0,q,visit)
            square, moves = q.popleft()

            for i in range(1, 7):
                
                nextSquare = square + i

                r, c = intToPos(nextSquare)

                if board[r][c] != -1:
                    nextSquare = board[r][c]

                if nextSquare == length * length:
                    return moves + 1

                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, moves + 1])

        return -1

        