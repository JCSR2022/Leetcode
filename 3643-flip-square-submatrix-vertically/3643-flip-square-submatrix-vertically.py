class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:


        for i in range(k//2):
            grid[x+k-1-i][y:y+k],grid[x+i][y:y+k] = grid[x+i][y:y+k] ,grid[x+k-1-i][y:y+k]
        return grid


        #  for i in range(k//2):
        #     temp  = grid[x+i][y:y+k]
        #     temp2 = grid[x+k-1-i][y:y+k]
        #     grid[x+k-1-i][y:y+k] = temp
        #     grid[x+i][y:y+k] = temp2
        #     print(i,x+i,x+k-1-i)
        #     print(temp)
        #     print(temp2)



        # return grid

       