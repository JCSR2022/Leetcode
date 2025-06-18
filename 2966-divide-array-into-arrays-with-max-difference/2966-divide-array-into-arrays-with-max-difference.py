class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        #brute force:
        #sort  nLog(n)
        # N = len(nums)
        # nums.sort()
        # ans=[[]]
        # for i in range(N):
        #     if not ans[-1]:
        #         ans[-1].append(nums[i])
        #         min_n = nums[i]
        #     else:
        #         if nums[i]-min_n > k:
        #             return []
        #         else:
        #             ans[-1].append(nums[i])
        #             if len(ans[-1]) ==3:
        #                 ans.append([])
        
        # return ans[:-1]

 #--------------------------------------------------------

        nums.sort()
        ans = []
        for i in range(0,len(nums),3):
            if nums[i+2] - nums[i] > k:
                return []
            ans.append(nums[i:i+3])
        return ans