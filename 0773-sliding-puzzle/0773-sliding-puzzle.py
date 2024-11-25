class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
#         states = set()
        
#         final = tuple([1,2,3,4,5,0])
#         ans = []
        
#         def convert_state(matrix):
#             return tuple(elem for row in matrix for elem in row)
        
#         def dfs(matrix,i,j,moves=0):
            
#             new_state = convert_state(matrix)

#             if new_state == final:
#                 ans.append(moves)
#                 return

#             if new_state in states:
#                 return
#             else:
#                 states.add(new_state)

#             #print(states)

#             #down
#             if i == 0 :
#                 matrix[0][j],matrix[1][j]=matrix[1][j], matrix[0][j]
#                 dfs(matrix,1,j,moves+1)
#                 matrix[0][j],matrix[1][j]=matrix[1][j], matrix[0][j]

#             #up
#             if i == 1 :
#                 matrix[1][j],matrix[0][j]=matrix[0][j], matrix[1][j]
#                 dfs(matrix,0,j,moves+1)
#                 matrix[1][j],matrix[0][j]=matrix[0][j], matrix[1][j]

#             #left
#             if j > 0:
#                 matrix[i][j],matrix[i][j-1] = matrix[i][j-1],matrix[i][j]  
#                 dfs(matrix,i,j-1,moves+1)
#                 matrix[i][j],matrix[i][j-1] = matrix[i][j-1],matrix[i][j]

#             #right
#             if j < 2:
#                 matrix[i][j],matrix[i][j+1] = matrix[i][j+1],matrix[i][j]  
#                 dfs(matrix,i,j+1,moves+1)
#                 matrix[i][j],matrix[i][j+1] = matrix[i][j+1],matrix[i][j]
                    
                
        
#         #find_ij_0:
#         ij_0 = [0,0]
#         for i,row in enumerate(board):
#             for j,elem in enumerate(row):
#                 if elem == 0:
#                     ij_0[0] = i
#                     ij_0[1] = j
                    
#         dfs(board,ij_0[0],ij_0[1])

        
#         return -1 if not ans else min(ans)

#------------------------------------------------------------------
#Khosiyat Sabir


        # Target state and initial state
            target = "123450"
            start = ''.join(str(num) for row in board for num in row)

            # Neighbors map for each index in the 1D representation of the board
            neighbors = {
                0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
                3: [0, 4], 4: [1, 3, 5], 5: [2, 4]
            }

            # BFS setup
            queue = deque([(start, 0)])  # (state, moves)
            visited = set()
            visited.add(start)

            while queue:
                state, moves = queue.popleft()

                # Check if we've reached the target
                if state == target:
                    return moves

                # Find the index of zero
                zero_index = state.index('0')

                # Generate new states by swapping '0' with its neighbors
                for neighbor in neighbors[zero_index]:
                    # Convert state to a list for mutation
                    new_state = list(state)
                    # Swap '0' with the neighbor
                    new_state[zero_index], new_state[neighbor] = new_state[neighbor], new_state[zero_index]
                    # Convert back to string
                    new_state_str = ''.join(new_state)

                    # If this new state hasn't been visited, add it to the queue
                    if new_state_str not in visited:
                        visited.add(new_state_str)
                        queue.append((new_state_str, moves + 1))

            # If we exhaust the queue without finding the target
            return -1