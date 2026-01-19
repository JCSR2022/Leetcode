class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:



        m = len(mat)
        n = len(mat[0])

        pre_sum = [ [0 for _ in range(n)] for _ in range(m)]


        for i in range(m):
            for j in range(n):
                pre_sum[i][j] = ( mat[i][j]
                    + (pre_sum[i][j-1] if j>0 else 0)
                    + (pre_sum[i-1][j] if i>0 else 0)
                    - (pre_sum[i-1][j-1] if i>0 and j>0 else 0)
                )

        
        def find_sum(i,j,size):

            return (    (pre_sum[i+size][j+size])

                        -(pre_sum[i-1][j+size] if i > 0  else 0)
                        -(pre_sum[i+size][j-1] if j > 0  else 0)               
                        # -(pre_sum[i-1][j+size] if i > 0 and j+size < m else 0)
                        # -(pre_sum[i+size][j-1] if j > 0 and i+size < n else 0)
                        +(pre_sum[i-1][j-1] if j >0 and i>0 else 0 )

            )

    
        ans = 0
        for i in range(m):
            for j in range(n):
                for k in range( min(n-j,m-i) ):
                    if find_sum(i,j,k) <= threshold: 
                        ans = max(ans,k+1)
                    else:
                        break
        
        return ans








        return 0
 
[1, 2, 5, 7, 11, 14, 16]
[2, 4, 10, 14, 22, 28, 32]
[3, 6, 15, 21, 33, 42, 48]


#----------------------------------------

        #brute force?

        # n = len(mat)
        # m = len(mat[0])


        # def sum_col(i,j,size):
        #     if i+size > n or j>=m:
        #         return -1
        #     return sum( mat[k][j] for k in range(i,i+size) )

        # def sum_row(i,j,size):
        #     if i>= n or j+size > m:
        #         return -1
        #     return sum( mat[i][k] for k in range(j,j+size-1) )


        # max_size = 0
        # for i in range(n):
        #     for j in range(m):
        #         cur_size = 0
        #         cur_sum = 0
        #         new_i = i
        #         new_j = j 
        #         while new_i < n and new_j < m and cur_sum <= threshold:
        #             max_size = max(max_size,cur_size)
        #             col = sum_col(i,new_j,cur_size)
        #             row = sum_row(new_i,j,cur_size)
        #             cur_sum += col+row
        #             cur_size +=1


        # return max_size

# Maldita sea @#%#$^%&$&$$*^&*^&^%&(%^&(^*%^^%))
#------------------------------------------------------------------------











                

        