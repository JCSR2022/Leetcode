class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:


        m = len(grid)
        n = len(grid[0])

        rows = [0]*m
        cols = [0]*n

        for i in range(m):
            for j in range(n):
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]


        #work on rows
        prefix = [0]*m
        prefix[0] = rows[0]
        for i in range(1,m):
            prefix[i] = prefix[i-1]+rows[i]

        sufix = [0]*m
        sufix[-1] = rows[-1]
        for i in range(m-2,-1,-1):
            sufix[i] = sufix[i+1]+rows[i] 

        for i in range(i,m-1):
            if prefix[i] == sufix[i+1]:
                return True


        #work on columns
        prefix = [0]*n
        prefix[0] = cols[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1]+cols[i]

        sufix = [0]*n
        sufix[-1] = cols[-1]
        for i in range(n-2,-1,-1):
            sufix[i] = sufix[i+1]+cols[i] 

        for i in range(i,n-1):
            if prefix[i] == sufix[i+1]:
                return True


        return False
            

        