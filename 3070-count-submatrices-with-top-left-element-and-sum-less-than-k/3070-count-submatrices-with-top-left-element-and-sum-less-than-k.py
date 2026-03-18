class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:

        #straigth forward

        # cnt = 0
        # n = len(grid)
        # m = len(grid[0])

        # col_sum = [0]*m
        # for i in range(n):
        #     cur_sum = 0
        #     for j in range(m):
        #         cur_sum += grid[i][j] + col_sum[j]
        #         print((i,j),grid[i][j],cur_sum,col_sum,cur_sum <= k,cnt+1)
        #         if cur_sum <= k:
        #             cnt += 1
        #             col_sum[j] = cur_sum 
        #         else:
        #             break

        
        # return cnt


#maldtio imbcil!!!! hasta cuando , no sirves para una maldita mierda!!!!!


        cnt = 0
        n = len(grid)
        m = len(grid[0])

        col_sum = [0]*m
        for i in range(n):
            cur_sum = 0
            for j in range(m):
                cur_sum += grid[i][j]
                if cur_sum+col_sum[j] <= k:
                    cnt += 1
                    col_sum[j] += cur_sum 
                    #print((i,j),cnt,col_sum )
                else:
                    col_sum[j] = k+1
                    break

        
        return cnt