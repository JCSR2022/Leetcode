class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        #bruteforce, realy bad  n**3//
        #backtrack
        #for each position evaluate 


        # n = len(board)

        # revese_board = board[::-1]
        # special_position = [0]*n**2
        # for i in range(n**2):
        #     if revese_board[i//n][i%n] > 0:
        #         special_position[i] = revese_board[i//n][i%n]
        # special_position = [0] + special_position

        # min_moves = [float("inf")]
        # memory = defaultdict(int)
        # def backtrack(position,moves):
        #     print(position,moves)

        #     if position >= n**2-1:
        #         min_moves[0] = min(min_moves[0],moves)
        #         return 

        #     if position in memory:
        #         if  memory[position] > moves:
        #             memory[position] = moves

        #             for i in range(1,7):
        #                 next_position = min(position+i,n**2) 
        #                 if special_position[next_position]:
        #                     next_position = special_position[next_position]
                        
        #                 backtrack(next_position,moves+1)
               
        # backtrack(1,0)
        # return min_moves[0]


#no sirves para una maldita mierda!!!!!!!!!!!!!!!!!
#------------------------------------------------------
            
        # n = len(board)
        # revese_board = board[::-1]
        # special_position = [0]*n**2
        # for i in range(n**2):
        #     if revese_board[i//n][i%n] > 0:
        #         special_position[i] = revese_board[i//n][i%n]
        #     else:
        #         special_position[i] = i+1
        # special_position = [0]+special_position+[0]

        # def bfs():
            
        #     heap = []
        #     heapq.heappush(heap, (0,1))

        #     while heap:
        #         print(heap)
        #         moves,position = heapq.heappop(heap)

        #         if position >= n**2:
        #             return moves

        #         if moves > n**2:
        #             return -1

        #         next_pos_set =set()
        #         normal = set()
        #         for i in range(1,7):
        #             next_pos = min(position + i, n**2+1) 
        #             if special_position[next_pos] == next_pos:
        #                 normal.add(next_pos)    
        #             else:
        #                 next_pos_set.add(special_position[next_pos])
        #         if normal:
        #             next_pos_set.add(max(normal))
            
        #         for next_position in next_pos_set:
        #             heapq.heappush(heap, (moves+1 ,next_position))

            
        # return bfs()



#por mil!!!!!!!!!!!!!!!!!!!
#muerete imbecil
#no sirves para una maldita mierda!!!!!!!!!!!!!!!!!
#------------------------------------------------------

        

        # n = len(board)

        # def get_position(s):
        #     """tablero Boustrophedon."""
        #     quot, rem = divmod(s - 1, n)
        #     row = n - 1 - quot
        #     col = rem if (n - 1 - row) % 2 == 0 else n - 1 - rem
        #     return row, col

        # heap = []
        # heapq.heappush(heap, (0,1)) #(número de movimientos,posición)
        # visited = set()

        # while heap:
        #     print(heap)
        #     moves, pos  = heapq.heappop(heap)

        #     if pos in visited:
        #         continue
        #     visited.add(pos)

        #     for i in range(1, 7):
        #         next_pos = pos + i
        #         if next_pos > n * n:
        #             break
        #         r, c = get_position(next_pos)
        #         if board[r][c] != -1:
        #             next_pos = board[r][c]
        #         if next_pos == n * n:
        #             return moves + 1
        #         if next_pos not in visited:
        #             heapq.heappush(heap, (moves + 1,next_pos))
          
        # return -1



#por cien mil!!!!!!!!!!!!!!!!!!!
#muerete imbecil, ya acabca con tu miserable vida pedazo de mierda!!!
#no sirves para una maldita mierda!!!!!!!!!!!!!!!!!
#------------------------------------------------------


        n = len(board)

        def get_position(s):
            quot, rem = divmod(s - 1, n)
            row = n - 1 - quot
            col = rem if (n - 1 - row) % 2 == 0 else n - 1 - rem
            return row, col

        visited = set()
        queue = deque([(1, 0)])  # (posición, número de movimientos)

        while queue:
            pos, moves = queue.popleft()

            next_pos_set = set()
            normal_pos = set()
            for i in range(1, 7):
                next_pos = pos + i

                if next_pos > n * n:
                    break
                
                r, c = get_position(next_pos)
                if board[r][c] != -1:
                    next_pos_set.add(board[r][c])
                else:
                    normal_pos.add(next_pos)

                if next_pos == n*n or (next_pos_set and n*n in next_pos_set ):
                    return moves + 1

            if normal_pos:
                next_pos_set.add(max(normal_pos))
            
            for next_pos in next_pos_set:
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, moves + 1))
        
        return -1




#---------------------------------------------------------------



        # n = len(board)

        # def get_position(s):
        #     """Convierte un número lineal s a coordenadas (r, c) en el tablero Boustrophedon."""
        #     quot, rem = divmod(s - 1, n)
        #     row = n - 1 - quot
        #     col = rem if (n - 1 - row) % 2 == 0 else n - 1 - rem
        #     return row, col

        # visited = set()
        # queue = deque([(1, 0)])  # (posición, número de movimientos)

        # while queue:
        #     pos, moves = queue.popleft()
        #     for i in range(1, 7):
        #         next_pos = pos + i
        #         if next_pos > n * n:
        #             continue
        #         r, c = get_position(next_pos)
        #         if board[r][c] != -1:
        #             next_pos = board[r][c]
        #         if next_pos == n * n:
        #             return moves + 1
        #         if next_pos not in visited:
        #             visited.add(next_pos)
        #             queue.append((next_pos, moves + 1))
        
        # return -1


#-----------------------------------------------------------

        # length = len(board)

        # def intToPos(square):

        #     square = square -1

        #     r = square//length
        #     if r%2 == 0:
        #         c = square%length
        #     else:
        #          c = length - square%length -1

        #     r = length - r -1

        #     return [r, c]

    
        # q = deque()
        # visit = set()
        # q.append([1,0])
        
        # while q:
        #     #print(0,q,visit)
        #     square, moves = q.popleft()

        #     for i in range(1, 7):
        #         #print(1,"dice:",i,"nextSquare:", square + i )

        #         nextSquare = square + i

        #         r, c = intToPos(nextSquare)

        #         if board[r][c] != -1:
        #             nextSquare = board[r][c]

        #         if nextSquare == length * length:
        #             return moves + 1

        #         if nextSquare not in visit:
        #             visit.add(nextSquare)
        #             q.append([nextSquare, moves + 1])

        # return -1

        