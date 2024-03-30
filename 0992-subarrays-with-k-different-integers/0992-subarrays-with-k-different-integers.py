class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
#         #brute force:
#         contGood = 0
#         contDiff = 0
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 contDiff = len(set(nums[i:j+1]))
#                 print(nums[i:j+1],contDiff == k)
#                 if contDiff == k:
#                     contGood +=1
        
#         return  contGood 
                    
        
        
        
        
        
        
        

        #sliding window (three pointers):
        def viewGoods(l_far,l_near,r):
            for i in range(l_far,l_near+1):
                print(nums[i:r+1],end = ', ' )
            print(l_far,l_near,r, l_near - l_far + 1 )
                
        
        count = defaultdict(int)
        ans = 0
        l_far = 0 
        l_near = 0
        
        for r in range(len(nums)):
            count[nums[r]] +=1
            
            # shrink if different integers > k
            while len(count) > k:
                count[nums[l_near]] -= 1
                if count[nums[l_near]] == 0:
                    count.pop(nums[l_near])
                l_near +=1
                l_far = l_near
                
            # shrink l_near if repited integers 
            while count[nums[l_near]] >1: 
                count[nums[l_near]] -=1
                l_near +=1
            
            if len(count) == k:
                #viewGoods(l_far,l_near,r)
                ans += l_near - l_far + 1 
        
        return ans
        
        
        
        
        
        