class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        #valid select if 0 and left = right  +-1

        # size = len(nums)
        # left = [0]*(size+1)
        # right = [0]*(size+1)

        # for i in range(size):
        #     left[i+1] = left[i]+nums[i]

        # for i in range(size-1,-1,-1):
        #     right[i] = right[i+1]+nums[i]

        # ans = 0
        # for i in range(size):
        #     if nums[i] == 0:
        #         if left[i+1] == right[i]:
        #             ans +=2
        #         elif abs(left[i+1] - right[i]) == 1:
        #             ans +=1
        # return ans


#------------------------------------------

        # size = len(nums)
        # left = [0]*(size+1)
        # right = [0]*(size+1)

        # for i in range(size):
        #     left[i+1] = left[i]+nums[i]
        #     right[size-i-1] = right[size-i]+nums[size-i-1]

        # ans = 0
        # for i in range(size):
        #     if nums[i] == 0:
        #         if left[i+1] == right[i]:
        #             ans +=2
        #         elif abs(left[i+1] - right[i]) == 1:
        #             ans +=1
        # return ans


#-------------------------------------------------------

       left_sum, right_sum = 0, sum(nums)
        ret = 0
        for num in nums:
            if num == 0:
                if 0 <= left_sum - right_sum <= 1:
                    ret += 1
                if 0 <= right_sum - left_sum <= 1:
                    ret += 1
            else:
                left_sum += num
                right_sum -= num
        return ret
        