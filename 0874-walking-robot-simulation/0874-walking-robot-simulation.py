class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
#         #brute force
#         #follow the robot
        
#         directions = [[0,1],[1,0],[0,-1],[-1,0]]
#         actual_pos = [0,0]
#         actual_dir = 0
        
        
#         def change_direc(commd,actual_dir):
#             if commd == -1:
#                 if actual_dir == 3:
#                     actual_dir = 0
#                 else:
#                     actual_dir += 1
#             elif commd == -2:
#                 if actual_dir == 0:
#                     actual_dir = 3
#                 else:
#                     actual_dir -= 1 
                    
#             return actual_dir
        
        
        
        
#         def advance(steps,actual_dir,actual_pos):    
#             while steps > 0:
#                 #print("###",steps,actual_dir,actual_pos)
#                 new_pos = [ actual_pos[0] + directions[actual_dir][0],actual_pos[1] + directions[actual_dir][1]]
#                 if new_pos not in obstacles:
#                     actual_pos = new_pos 
#                 steps -=1
#             return actual_pos
#             #print("###",actual_pos)
        
        
        
        
#         for commd in commands:
#             print(commd,directions[actual_dir],actual_pos)
#             if commd < 0:
#                 actual_dir = change_direc(commd,actual_dir)
#             else:
#                 actual_pos = advance(commd,actual_dir,actual_pos)
                
                
                
#         return actual_pos[0]**2 +actual_pos[1]**2
                
        
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Initialize position and direction
        x, y, direction = 0, 0, 0
        # Convert obstacles to a set for O(1) lookups
        obstacle_set = set(map(tuple, obstacles))
        # Initialize max distance
        max_distance = 0
        
        # Process each command
        for command in commands:
            if command == -1:  # Turn right
                direction = (direction + 1) % 4
            elif command == -2:  # Turn left
                direction = (direction - 1) % 4
            else:  # Move forward
                for _ in range(command):
                    # Calculate next position
                    next_x = x + directions[direction][0]
                    next_y = y + directions[direction][1]
                    # Check if next position is an obstacle
                    if (next_x, next_y) in obstacle_set:
                        break
                    # Update position
                    x, y = next_x, next_y
                    # Update max distance
                    max_distance = max(max_distance, x*x + y*y)
        
        return max_distance      
        
        
        