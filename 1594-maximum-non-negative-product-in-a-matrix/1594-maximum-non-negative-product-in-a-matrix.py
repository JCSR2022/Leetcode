class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:


        """
        bfs??
        """
        # mod = 10**9+7

        # m = len(grid)
        # n = len(grid[0])

        # heap = [(-grid[0][0],0,0)]

        # ans = -1
        # while heap:
        #     val, row_node,col_node = heapq.heappop(heap)
        #     val *=-1

        #     if row_node == m-1 and col_node == n-1 and val >=0:
        #         ans = max(ans,val)
        #         continue

        #     if  row_node < m-1:
        #         heapq.heappush(heap, (-1*val*grid[row_node+1][col_node],row_node+1,col_node))

        #     if col_node < n-1:
        #         heapq.heappush(heap, (-1*val*grid[row_node][col_node+1],row_node,col_node+1))
 
        # return ans%mod if ans>0 else ans

#Time Limit Exceeded
#-------------------------------------------------------------------------------       

        """
        using dp??
        """

        # mod = 10**9+7
        # m = len(grid)
        # n = len(grid[0])
        
        
        # dp_max = [ [ 0 for _ in range(n)] for _ in range(m)]
        # dp_min = [ [ 0 for _ in range(n)] for _ in range(m)]

        # dp_max[0][0] = grid[0][0]
        # dp_min[0][0] = grid[0][0]
        
        # for i in range(m):
        #     for j in range(n):
        #         if i-1>0 and j-1>0:
        #             dp_max[i][j] = max( dp_max[i][j-1]*grid[i][j],
        #                                 dp_max[i-1][j]*grid[i][j],
        #                                 dp_min[i][j-1]*grid[i][j],
        #                                 dp_min[i-1][j]*grid[i][j])

        #             dp_min[i][j] = min( dp_max[i][j-1]*grid[i][j],
        #                                 dp_max[i-1][j]*grid[i][j],
        #                                 dp_min[i][j-1]*grid[i][j],
        #                                 dp_min[i-1][j]*grid[i][j])
        #         elif i-1>0:
        #             dp_max[i][j] = max( dp_max[i][j-1]*grid[i][j],
        #                                 dp_min[i][j-1]*grid[i][j]
        #                                 )
        #             dp_min[i][j] = min( dp_max[i][j-1]*grid[i][j],
        #                                 dp_min[i][j-1]*grid[i][j]
        #                                 )
        #         elif j-1>0:
        #             dp_max[i][j] = max( dp_max[i-1][j]*grid[i][j],
        #                                 dp_min[i-1][j]*grid[i][j])

        #             dp_min[i][j] = min( dp_max[i-1][j]*grid[i][j],
        #                                 dp_min[i-1][j]*grid[i][j])

        # if dp_max[-1][-1]>0:
        #     return  dp_max[-1][-1]%mod
        # else:
        #     return -1
#maldito imbecil!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#----------------------------------------------------------------

        mod = 10**9+7
        m = len(grid)
        n = len(grid[0])
        
        dp_max = [ [0]*n for _ in range(m)]
        dp_min = [ [0]*n for _ in range(m)]

        dp_max[0][0] = grid[0][0]
        dp_min[0][0] = grid[0][0]
        
        for i in range(m):
            for j in range(n):
                if i ==0  and j == 0 :
                    continue

                if i == 0:
                    dp_max[i][j] =  dp_max[i][j-1]*grid[i][j]
                    dp_min[i][j] =  dp_min[i][j-1]*grid[i][j]

                if j == 0:
                    dp_max[i][j] =  dp_max[i-1][j]*grid[i][j]
                    dp_min[i][j] =  dp_min[i-1][j]*grid[i][j]

                else:
                    dp_max[i][j] = max( dp_max[i][j-1]*grid[i][j],
                                        dp_max[i-1][j]*grid[i][j],
                                        dp_min[i][j-1]*grid[i][j],
                                        dp_min[i-1][j]*grid[i][j])

                    dp_min[i][j] = min( dp_max[i][j-1]*grid[i][j],
                                        dp_max[i-1][j]*grid[i][j],
                                        dp_min[i][j-1]*grid[i][j],
                                        dp_min[i-1][j]*grid[i][j])
        
        if dp_max[-1][-1]>=0:
            return  dp_max[-1][-1]%mod
        else:
            return -1









        