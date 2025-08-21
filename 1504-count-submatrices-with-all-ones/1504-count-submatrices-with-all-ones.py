class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        
        # #brute force
        # m = len(mat)
        # n = len(mat[0])

        # for i in range(m):
        #     for j in range(n):
                



        # return 17


        r, c = len(mat), len(mat[0])
        h = [0] * c
        ans = 0
        for i in range(r):
            for j in range(c):
                h[j] = h[j] + 1 if mat[i][j] else 0
            sumv, st = [0] * c, []
            for j in range(c):
                while st and h[st[-1]] >= h[j]:
                    st.pop()
                if st:
                    p = st[-1]
                    sumv[j] = sumv[p] + h[j] * (j - p)
                else:
                    sumv[j] = h[j] * (j + 1)
                st.append(j)
                ans += sumv[j]
        return ans  
        