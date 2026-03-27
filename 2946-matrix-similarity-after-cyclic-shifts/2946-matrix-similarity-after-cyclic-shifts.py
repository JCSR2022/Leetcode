class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:

        # m = len(mat)
        # n = len(mat[0])

        # for i in range(m):
        #     for j in range(n):
        #         print(i,j,mat[j],mat[ (j-k)%n],mat[ (j+k)%n])
        #         if i%2 == 0:
        #             if mat[i][j] != mat[i][ (j-k)%n]:
        #                 return False
        #         else:
        #             if mat[i][j] != mat[i][ (j+k)%n]:
        #                 return False

        # return True
        

        m, n = len(mat), len(mat[0])
        
        k %= n  # (reduce k<n)
        
        for i in range(m):
            for j in range(n):
                if i % 2 == 0:
                    # even row , left shift
                    if mat[i][j] != mat[i][(j + k) % n]:
                        return False
                else:
                    # odd row , right shift
                    if mat[i][j] != mat[i][(j - k) % n]:
                        return False
        
        return True