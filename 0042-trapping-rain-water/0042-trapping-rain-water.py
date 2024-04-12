class Solution:
    def trap(self, height: List[int]) -> int:
 
        #First solve:
#         if not height: return 0
    
#         l,r = 0, len(height)-1
#         leftMax, rightMax = height[l],height[r]
#         ans = 0
        
#         while l < r:
#             if leftMax < rightMax:
#                 l +=1
#                 leftMax = max(leftMax, height[l])
#                 ans += leftMax - height[l]
#             else:
#                 r -=1
#                 rightMax = max(rightMax,height[r])
#                 ans += rightMax - height[r]
                
#         return ans
                

# -------------------------------------------------------------------


        def max_left_height(i):
            if i < 1:
                return 0
            return max(height[:i])

        def max_right_height(i):
            if i > len(height)-2:
                return 0
            return max(height[i+1:])

        max_left_vect = []
        for i in range(len(height)):
            max_left_vect.append(max_left_height(i))
        
        max_right_vect = []
        for i in range(len(height)):
            max_right_vect.append(max_right_height(i))
        
        water = 0
        for i,h in enumerate(height): 
            water += max(min(max_left_vect[i] ,max_right_vect[i])-h,0)
        
        return water
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def max_left_height(i):
#             if i < 1:
#                 return 0
#             return max(height[:i])

#         def max_right_height(i):
#             if i > len(height)-2:
#                 return 0
#             return max(height[i+1:])

        
#         water = 0
#         for i,h in enumerate(height):
#             #print(height,i,'max_left:',max_left_height(i) ,'max_right:',max_right_height(i), max(min(max_left_height(i) ,max_right_height(i))-h,0))  
#             water += max(min(max_left_height(i) ,max_right_height(i))-h,0)
        
#         return water