class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for num in nums:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)
        
        ans = [ pos.pop(0) if i%2 ==0 else  neg.pop(0) for i in range(len(nums))]
        
        return ans
                
        