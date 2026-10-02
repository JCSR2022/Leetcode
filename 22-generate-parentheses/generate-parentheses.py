class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        list_ans = []
        def dfs(ans,cnt_open, cnt_close):
            if cnt_close == 0:
                list_ans.append(ans)

            if cnt_open > 0:
                dfs(ans+"(",cnt_open-1, cnt_close)

            if cnt_close > cnt_open:
                dfs(ans+")",cnt_open, cnt_close-1)

        dfs("",n,n)
        return list_ans
 
        