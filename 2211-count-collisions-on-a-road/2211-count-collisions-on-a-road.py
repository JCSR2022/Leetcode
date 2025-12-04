class Solution:
    def countCollisions(self, directions: str) -> int:

        

        directions = directions.lstrip("L")
        directions = directions.rstrip("R")

        return directions.count("R") + directions.count("L")









        
        # prev = 'R'
        # collisions = 0
        # cars = 0
        # for move in directions: 
        #     if move == 'R' and prev = 'R':
        #         cars +=1
        #     elif move == 'L' and prev = 'R':
        #         collisions += cars + 1 
        #         cars = 0
        #     elif move == 'S' and prev = 'R':
        #         collisions += cars  
        #         cars = 0
        #     elif move == 'R' and prev = 'S':
        #         cars = 1
        #     elif move == 'L' and prev = 'S':
        #         pass    
        #     elif move == 'S' and prev = 'S':
        #         pass
        #     elif move == 'R' and prev = 'L':
        #         pass
        #     elif move == 'L' and prev = 'L':
        #         pass
        #     elif move == 'S' and prev = 'L':
        #         pass
        
            