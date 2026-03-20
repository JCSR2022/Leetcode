class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:

        #brute force

        m = len(grid)
        n = len(grid[0])

        ans = [ [0 for _ in range(n-k+1) ] for _ in range(m-k+1)] 

        def find_arr(i,j):
            arr = set()
            for x in range(i,i+k):
                for y in range(j,j+k):
                    arr.add(grid[x][y])
            return list(arr)

        def min_absolute(arr):
            if len(arr) == 1:
                return 0
            arr.sort()
            min_abs = float('inf')
            for i in range(len(arr)-1):
                min_abs = min(min_abs,abs(arr[i]-arr[i+1]))
            return min_abs

        for i in range(m-k+1):
            for j in range(n-k+1):
                ans[i][j] = min_absolute(find_arr(i,j))
                arr = find_arr(i,j)
                #print(arr , min_absolute(arr))

        return ans
        