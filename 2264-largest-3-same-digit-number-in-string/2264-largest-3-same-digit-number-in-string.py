class Solution:
    def largestGoodInteger(self, num: str) -> str:

        #craizy sol

        count = [-1,0]  # [digit, count on digit]
        ans = -1
        for n in num:
            if n == count[0]:
                count[1] += 1
            else:
                count[0],count[1] = n,1
            if count[1] == 3:
                ans = max(ans,int(count[0]))

        return str(ans)*3 if ans >= 0 else ""


        

        