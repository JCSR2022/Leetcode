class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # ans = []
        # for i in range(n):
        #     ans.append(nums[i])
        #     ans.append(nums[n+i])

        # return ans
#----------------------------------------------------------

        ans = []
        for x,y in zip(nums[:n],nums[n:]):
            ans.append(x)
            ans.append(y)

        return ans