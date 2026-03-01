class Solution:
    def minPartitions(self, n: str) -> int:
        
        # ans = '0'
        # for ch in n:
        #     ans = max(ans,ch)
        #     if ans == '9':
        #         return 9
        # return int(ans)
        

        for d in "987654321":
            if d in n:
                return int(d)