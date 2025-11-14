class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        #brute force

        ans = [ [0]*n for _ in range(n)]

        for row1i, col1i, row2i, col2i in queries :
            for j in range(col1i,col2i+1):
                for i in range(row1i,row2i+1):
                    ans[i][j] +=1
            # print(row1i, col1i, row2i, col2i)
            # for row in ans:
            #     print(row)
            # print()
        return ans