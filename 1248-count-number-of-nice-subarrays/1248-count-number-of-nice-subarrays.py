class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        # 3 pointers sliding window 
        
        l = 0
        m = 0
        
        ans = 0 
        odds = 0
        
        for r in range(len(nums)):
            if nums[r] % 2:
                odds +=1
                
            while odds > k :
                if nums[l] %2:
                    odds -= 1
                l += 1
                m = l
                
            if odds == k:
                while not nums[m] % 2:
                    m += 1
                ans += m - l + 1
                    
        return ans
        
        
        
        
        
        
        
        
        #slading window O(n), do not work
        
#         # def isNice(arr,k):
#         #     count = 0
#         #     for n in arr:
#         #         if n%2 != 0:
#         #             count += 1
#         #     if count == k:
#         #         return True
#         #     return False
        
        
#         def countOdds(arr):
#             count = 0
#             for n in arr:
#                 if n%2 != 0:
#                     count += 1
#             return count      
        
        
#         l = 0
#         r = 0
        
#         ans = 0
#         while r < len(nums):
#             co = countOdds(nums[l:r])
#             print(nums[l:r],co,ans)
#             if co == k:
#                 ans += 1
#                 r += 1
#             elif co < k:
#                 r += 1
#             elif co > k:
#                 l += 1
                
#         while l < r:
#             co = countOdds(nums[l:r]) 
#             print(nums[l:r],co,ans)
#             if co == k:
#                 ans += 1
#             l +=1
        
#         return ans
                
        
        
        
        
        
        
#         #brute force O(n**2)

#         def countOdds(arr):
#             count = 0
#             for n in arr:
#                 if n%2 != 0:
#                     count += 1
#             return count                    
#         ans = 0
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 print(nums[i:j+1],countOdds(nums[i:j+1])==k)
#                 if countOdds(nums[i:j+1])==k:
#                     ans +=1
#         return ans
        