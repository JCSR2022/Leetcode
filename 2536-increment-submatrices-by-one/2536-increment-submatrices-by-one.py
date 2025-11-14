class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        #brute force

        # ans = [ [0]*n for _ in range(n)]

        # for row1i, col1i, row2i, col2i in queries :
        #     for j in range(col1i,col2i+1):
        #         for i in range(row1i,row2i+1):
        #             ans[i][j] +=1
        #     # print(row1i, col1i, row2i, col2i)
        #     # for row in ans:
        #     #     print(row)
        #     # print()
        # return ans

#Time Limit Exceeded
#-------------------------------------------------------------------

        ans = [ [0]*(n+1) for _ in range(n)]

        for row1i, col1i, row2i, col2i in queries :
            for i in range(row1i,row2i+1):
                ans[i][col1i] +=1
                ans[i][col2i+1] -=1
                
            # print(row1i, col1i, row2i, col2i)
            # for row in ans:
            #     print(row)
            # print()

        for row in ans:
            for j in range(n):
                row[j+1] = row[j+1]+row[j]     

        return [ row[:-1] for row in ans]

#--------------------------------------------------0
        #This will not work logic is bad

        # pre_ans = [0]*((n**2)+1)
        # for row1i, col1i, row2i, col2i in queries :
        #     pre_ans[row1i*n+ col1i ] +=1
        #     pre_ans[row2i*n+ col2i+1 ] -=1

        # print(pre_ans)


        # ans = [ [0]*n for _ in range(n)]
        # return ans






