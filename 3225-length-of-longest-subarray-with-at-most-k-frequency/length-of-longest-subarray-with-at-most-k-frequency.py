class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        #sliding window

        size = len(nums)
        frec = defaultdict(int)
        length = 0
        max_length = 0
        i = 0
        j = 0
        while j < size:
            frec[nums[j]] +=1
            length +=1
            while frec[nums[j]] > k:
                frec[nums[i]] -=1
                i +=1
                length -=1
            j +=1
            max_length = max(max_length,length)

        return max_length
        





        