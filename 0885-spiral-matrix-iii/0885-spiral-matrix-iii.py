class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        """Approach:
        1. We simulate a spiral movement starting from the given (rStart, cStart) coordinate.
        2. The movement pattern is as follows:
           - Move right, down, left, and up in a cyclic order.
           - After every two directions (right/down and left/up), increase the steps taken in each direction by one.
        3. As we move, we check if the current cell is within the matrix bounds.
           If it is, we add it to the visited list and continue until we've visited all cells.
        
        Time Complexity Analysis:
        - The total number of cells we need to visit is `rows * cols`.
        - The movement pattern ensures that each cell is visited once.
        - The loop continues until we've visited all cells, which results in O(N) time complexity,
          where the max N is (2*rows * 2*cols).

        Space Complexity Analysis:
        - The space complexity is primarily driven by the output list `visited`, which stores the coordinates.
        - Since we store each of the N coordinates exactly once, the space complexity is O(N), in this case
        N = rows * cols.
        """
        
        
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
                
            
            
            
            
            