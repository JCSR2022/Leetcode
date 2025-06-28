import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        #aproach, make a heap of size k, change 
        #no, will not work 

        #sort arr by val and index? will not work nether

        #sorted arr to save ans?
        # why not min_heap?
        #if len(ans)<k, heappuesh
        # if n > ans[0] ,heapopush

        ans = []
        for i,n in enumerate(nums):
            if len(ans) < k:
                heapq.heappush(ans,(n,i))
            else:
                if n > ans[0][0]:
                    heapq.heappushpop(ans,(n,i))

        return [ n for n,i in sorted(ans,key=lambda x:x[1])]
        
            




