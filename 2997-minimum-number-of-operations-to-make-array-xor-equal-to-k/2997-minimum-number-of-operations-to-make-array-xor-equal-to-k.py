class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        
        t = 0 
        for x in nums:
            t ^= x
            print(x,t)
        t ^= k
        
        r = 0 
        while t > 0:
            r += t % 2
            t //= 2
        
        return r
        