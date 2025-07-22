class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        #two pointers and hash

        hash_sub = defaultdict(int)
        max_sum = 0
        cur_sum = 0
        l = 0
        for r in range(len(nums)):
            hash_sub[nums[r]] += 1
            while hash_sub[nums[r]] > 1:
                cur_sum -= nums[l]
                hash_sub[nums[l]] -= 1
                l += 1

            cur_sum += nums[r]
            max_sum = max(max_sum,cur_sum)
            #print(dict( hash_sub),cur_sum, max_sum)

        return max_sum