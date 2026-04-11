class Solution:
    def minimumDistance(self, nums: List[int]) -> int:

        # aproach, n*log(n) do to sort
        # make a hash list of repeted num in nums saving the indexes
        # sort the list of indexs beacause we are lokong the closest
        #use a sliding window size 3 to find min

        hash_nums = defaultdict(list)
        for i in range(len(nums)):
            hash_nums[nums[i]].append(i)

        ans = float("inf")
        for list_idx in hash_nums.values():
            if len(list_idx) >= 3:
                list_idx.sort()
                for i in range(2,len(list_idx)):
                    ans = min(ans, 2*(list_idx[i]-list_idx[i-2]))
        
        if ans == float("inf"):
            return -1

        return ans





        