class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:

        # prev_sec = 1
        # curr_sec = 0
        # prev_num = float("-inf")
        # max_sec = 1
        # for n in nums:
        #     if n > prev_num:
        #         curr_sec += 1
        #     else:
        #         prev_sec = curr_sec
        #         curr_sec = 1

        #     prev_num = n
        #     max_sec = min(prev_sec,curr_sec)

        # return max_sec


        n = len(nums)
        up, preUp, res = 1, 0, 0
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                up += 1
            else:
                preUp = up
                up = 1
            half = up >> 1
            m = min(preUp, up)
            candidate = max(half, m)
            if candidate > res:
                res = candidate
        return res


        