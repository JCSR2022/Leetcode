class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        
        
        directions = [0, 1, 0, -1, 0]
        res = [[rStart, cStart]]
        j = n = 0
        while len(res) < rows * cols:
            for i in range(n // 2 + 1):
                rStart += directions[j]
                cStart += directions[j + 1]
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
            n += 1
            j = (j + 1) % 4
        return res
        
        # aproach, brute force?:  
        # time complex  O(n), max  rStart = rows-1, cStart = cols-1, (2*rows)*(2*cols)
        # move in espiral , every 2 move add 1 to the steps
        # check if valid cell 
        
        
#         self.cont_visited = 1
#         self.visited = [[rStart,cStart]]
        
#         def checkValid(r,c):          
#             if r < rows and r >= 0 and c < cols and c >= 0:
#                 self.cont_visited +=1
#                 self.visited.append([r,c])
                
        
#         size = rows*cols
#         steps = 0
#         r = rStart
#         c = cStart
    
#         while self.cont_visited < size:

#             steps +=1
#             #move to right
#             for _ in range(steps):
#                 c += 1
#                 checkValid(r,c)
#             #move down
#             for _ in range(steps):
#                 r += 1
#                 checkValid(r,c)
                
#             steps +=1
#             #move left
#             for _ in range(steps):
#                 c -= 1
#                 checkValid(r,c)
#             #move up
#             for _ in range(steps):
#                 r -= 1
#                 checkValid(r,c)
            
#         return self.visited
                
            
            
            
            
            