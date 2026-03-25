class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:





        #aproach  O(n*m +n+m)

        m = len(grid)
        n = len(grid[0])

        rows = [0]*m
        cols = [0]*n
        total = 0

        for i in range(m):
            for j in range(n):
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]
                total += grid[i][j]

        if total%2 != 0:
            return False
        half = total//2

        #work on rows
        prefix = 0
        for row in rows:
            prefix += row
            if prefix == half:
                return True
            if prefix > half:
                break

        prefix = 0
        for col in cols:
            prefix += col
            if prefix == half:
                return True
            if prefix > half:
                break

        return False


#--------------------------------------------------------
        # #aproach  O(n*m + 3*n +3*m)

        # m = len(grid)
        # n = len(grid[0])

        # rows = [0]*m
        # cols = [0]*n

        # for i in range(m):
        #     for j in range(n):
        #         rows[i] += grid[i][j]
        #         cols[j] += grid[i][j]


        # #work on rows
        # prefix = [0]*m
        # prefix[0] = rows[0]
        # for i in range(1,m):
        #     prefix[i] = prefix[i-1]+rows[i]

        # sufix = [0]*m
        # sufix[-1] = rows[-1]
        # for i in range(m-2,-1,-1):
        #     sufix[i] = sufix[i+1]+rows[i] 

        # for i in range(i,m-1):
        #     if prefix[i] == sufix[i+1]:
        #         return True


        # #work on columns
        # prefix = [0]*n
        # prefix[0] = cols[0]
        # for i in range(1,n):
        #     prefix[i] = prefix[i-1]+cols[i]

        # sufix = [0]*n
        # sufix[-1] = cols[-1]
        # for i in range(n-2,-1,-1):
        #     sufix[i] = sufix[i+1]+cols[i] 

        # for i in range(i,n-1):
        #     if prefix[i] == sufix[i+1]:
        #         return True


        # return False
            

        