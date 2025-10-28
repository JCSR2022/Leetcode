class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        #valid select if 0 and left = right  +-1
        size = len(nums)
        left = [0]*(size+1)
        right = [0]*(size+1)

        for i in range(size):
            left[i+1] = left[i]+nums[i]

        for i in range(size-1,-1,-1):
            right[i] = right[i+1]+nums[i]

        # print(left)
        # print(right)

        ans = 0
        for i in range(size):
            if nums[i] == 0:
                if left[i+1] == right[i]:
                    ans +=2
                elif abs(left[i+1] - right[i]) == 1:
                    ans +=1
        return ans




        