class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        
        # aproach: 
        # create matrix center in rstart and cStart
        # move in espiral , every 2 move add 1 to the stepst to do
        
        
        self.cont_visited = 1
        self.visited = [[rStart,cStart]]
        
        def checkValid(r,c):          
            if r <= rows-1 and r >= 0 and c <= cols-1 and c >= 0:
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
            for _ in range(steps):
                c -= 1
                checkValid(r,c)
            for _ in range(steps):
                r -= 1
                checkValid(r,c)
            
        return self.visited
                
            
            
            
            
            