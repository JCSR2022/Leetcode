class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        # brute force n**2:
        
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         #print(i,j,nums[i:j+1])
        #         if sum(nums[i:j+1])%k == 0:
        #             return True
        # return False
    
    
        # hashMap :https://www.youtube.com/watch?v=OKcrLfR-8mE
        
        remainder = {0:-1}
        total = 0
        
        for i,n in enumerate(nums):
            total += n
            r = total % k 
            
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True
        return False
        