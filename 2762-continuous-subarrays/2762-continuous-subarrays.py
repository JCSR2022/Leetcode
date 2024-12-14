class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        
        #brute force  O(n**2)
#         ans = 0    
        
#         for i in range(len(nums)):
#             my_min = nums[i]
#             my_max = nums[i]
#             for j in range(i,len(nums)):
#                 my_min = min(my_min,nums[j])
#                 my_max = max(my_max,nums[j])
#                 if my_max-my_min<=2:
#                     ans +=1
#                 else:
#                     break
#         return ans
    
    #evidently Time Limit Exceeded
#------------------------------------------------------    

# sliding window 

#         L = 0 
#         R = 0
#         min_in_wind = nums[L]
#         max_in_wind = nums[L] 
#         ans = 0
        
#         for R in range(len(nums)):
#             min_in_wind = min(min_in_wind,nums[R])
#             max_in_wind = max(max_in_wind,nums[R])
#             #print(L,R,nums[L:R+1])
#             if max_in_wind - min_in_wind > 2:
#                 size = R-L
#                 ans += size*(size+1)//2
#                 #print("size,ans:",size,ans)
#                 L = R
#                 while abs(nums[R]-nums[L]) <= 2:
#                     #print(L,R)
#                     L -= 1 
#                     #print(L,R,nums[L],nums[R],abs(nums[R]-nums[L]) < 2)
#                 L += 1
                
#                 size = R-L
#                 ans -= size*(size+1)//2
#         size = R-L
#         ans += size*(size+1)//2       
        
#         return ans
                
#need to fix #@%#@^$#$^$%$&%*%$$%^^*%^$#&#$^@#@
#-----------------------------------------------------


#ni se que hace esto            
#         l, r = nums[0] - 2, nums[0] + 2
#         lo, ans = -1, 0
#         for hi, x in enumerate(nums):
#             if l <= x <= r:
#                 l, r = max(l, x - 2), min(r, x + 2)
#             else:
#                 l, r = x - 2, x + 2
#                 lo = hi - 1
#                 while l <= nums[lo] <= r:
#                     l, r = max(l, nums[lo] - 2), min(r, nums[lo] + 2)
#                     lo -= 1    
#             ans += hi - lo
#         return ans 
            
        
#---------------------------------------------

        i = res = 0
        d = dict()
        for j, num in enumerate(nums):
            t = d.copy()
            for k, v in t.items():
                if abs(k - num) > 2:
                    i = max(i, v + 1)
                    d.pop(k)
            d[num] = j
            res += j - i + 1
        return res
