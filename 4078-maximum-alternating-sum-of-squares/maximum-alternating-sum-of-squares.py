class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        nums[:] = [abs(n) for n in nums]
        nums.sort(reverse = True)
        i = 0
        j = len(nums)-1
        ans = 0
        turn_i = True
        while j>=i:
            if turn_i:
                ans += nums[i]**2
                i +=1
                turn_i = False
            else:
                ans -= nums[j]**2
                j -=1
                turn_i = True
        return ans

        