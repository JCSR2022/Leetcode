class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:

        #brute force:

        cnt = 0
        for li,ri in queries:
            change = False
            for i in range(li,ri+1):
                if nums[i] > 0: 
                   nums[i] -= 1
                   change = True 
            if not change:
                cnt += 1

        if sum(nums) == 0:
            return cnt
        else:
            return -1

            

        