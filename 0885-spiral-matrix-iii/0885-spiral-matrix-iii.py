class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        
        
    
        visited_count = 1
        visited = [[rStart, cStart]]
        
        def is_valid(r, c):
            """Checks if the cell (r, c) is within the matrix bounds and, if so, adds it to the visited list."""
            if 0 <= r < rows and 0 <= c < cols:
                nonlocal visited_count
                visited_count += 1
                visited.append([r, c])
        
        total_cells = rows * cols
        steps = 0
        r, c = rStart, cStart
        
        # Spiral movement logic
        while visited_count < total_cells:
            steps += 1
            # Move right
            for _ in range(steps):
                c += 1
                is_valid(r, c)
            # Move down
            for _ in range(steps):
                r += 1
                is_valid(r, c)
            
            steps += 1
            # Move left
            for _ in range(steps):
                c -= 1
                is_valid(r, c)
            # Move up
            for _ in range(steps):
                r -= 1
                is_valid(r, c)
            
        return visited
        
        
        # directions = [0, 1, 0, -1, 0]
        # res = [[rStart, cStart]]
        # j = n = 0
        # while len(res) < rows * cols:
        #     for i in range(n // 2 + 1):
        #         rStart += directions[j]
        #         cStart += directions[j + 1]
        #         if 0 <= rStart < rows and 0 <= cStart < cols:
        #             res.append([rStart, cStart])
        #     n += 1
        #     j = (j + 1) % 4
        # return res
        
        # aproach, brute force?:  
        # time complex  O(n), max  rStart = rows-1, cStart = cols-1, (2*rows)*(2*cols)
        # move in espiral untill count of visited , every 2 move add 1 to the steps
        # check if valid cell, if valid add to visited, increment count of visited
        
        
        self.cont_visited = 1
        self.visited = [[rStart,cStart]]
        
        def checkValid(r,c):          
            if r < rows and r >= 0 and c < cols and c >= 0:
                self.cont_visited +=1
                self.visited.append([r,c])
                
        
        size = rows*cols
        steps = 0
        r = rStart
        c = cStart
    
        while self.cont_visited < size:

            steps +=1
            #move to right
            for _ in range(steps):
                c += 1
                checkValid(r,c)
            #move down
            for _ in range(steps):
                r += 1
                checkValid(r,c)
                
            steps +=1
            #move left
            for _ in range(steps):
                c -= 1
                checkValid(r,c)
            #move up
            for _ in range(steps):
                r -= 1
                checkValid(r,c)
            
        return self.visited
                
            
            
            
            
            