class Solution:
     def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:


        def helper(x):
            if x < 0: return 0
            
            ans = 0 
            l,currentTotal = 0,0
            
            for r in range(len(nums)):
                currentTotal += nums[r]
                
                while currentTotal > x:
                    currentTotal -= nums[l]
                    l +=1
                ans += r-l+1
                
            return ans 
            
            
        return helper(goal)-helper(goal -1)
        


        
#         # especial
#         if len(nums) <= 1:
#             return 0
        
#         if sum(nums) == 0:
#             return "Muerete"
        
#         # Sliding Window
#         L = 0
#         R = 0
#         cont = 0
        
#         while R < len(nums):
#             if L > R:
#                 print(L,R)
#                 R +=1
#                 continue
                
#             actual = sum(nums[L:R+1])
            
            
#             if actual == goal:
#                 cont +=1
#                 print(L,R,nums[L:R+1],actual,cont)
#                 R +=1 
                
#             if actual < goal:
#                 print(L,R,nums[L:R+1],actual,cont)
#                 R +=1
                
#             if actual >goal:
#                 print(L,R,nums[L:R+1],actual,cont)
#                 L +=1
        
#         while actual >= goal and L < len(nums)-1:
#             L += 1
#             actual = sum(nums[L:R+1])
#             if actual ==goal:
#                 cont +=1
#                 print("2: ",L,R,nums[L:R+1],actual,cont)

#         print("3: ",L,R,nums[L:R+1],actual,cont)
#         return cont
                    
                
        
                
            
            
            
                
            
        
        