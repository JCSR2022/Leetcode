class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # bruteforce hasmap O(n):
        
        hasMap = {}
        for n in nums:
            if n in hasMap:
                hasMap[n] += 1
            else:
                hasMap[n] = 1
        
        
        i = 0        
        for color in [0,1,2]:
            if color in hasMap:
                for j in range(i,i+hasMap[color]):
                    nums[j] = color
                i += hasMap[color] 
        
        
            