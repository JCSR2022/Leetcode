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


#         def max_left_height(i):
#             if i < 1:
#                 return 0
#             return max(height[:i])

#         def max_right_height(i):
#             if i > len(height)-2:
#                 return 0
#             return max(height[i+1:])

#         max_left_vect = []
#         for i in range(len(height)):
#             max_left_vect.append(max_left_height(i))
        
#         max_right_vect = []
#         for i in range(len(height)):
#             max_right_vect.append(max_right_height(i))
        
#         water = 0
#         for i,h in enumerate(height): 
#             water += max(min(max_left_vect[i] ,max_right_vect[i])-h,0)
        
#         return water
        
#         max_left_vect = []
#         act_max = 0
#         for h in height:
#             act_max = max(act_max,h)
#             max_left_vect.append(act_max)
#         max_left_vect = [0] + max_left_vect[:-1]     
        
        
#         max_right_vect = []
#         act_max = 0
#         for h in height[::-1]:
#             act_max = max(act_max,h)
#             max_right_vect.append(act_max)
#         max_right_vect[:] = max_right_vect[::-1]        
#         max_right_vect[:] = max_right_vect[1:]+[0]
        
        
#         water = 0
#         for i,h in enumerate(height): 
#             water += max(min(max_left_vect[i] ,max_right_vect[i])-h,0)
        
#         return water       
        
        l_wall = 0
        r_wall = 0
        max_left_vect = [0]*len(height)
        max_right_vect = [0]*len(height)
        
        for i in range(len(height)):
            j = -i-1
            max_left_vect[i] = l_wall
            max_right_vect[j] = r_wall
            l_wall = max(l_wall,height[i])
            r_wall = max(r_wall,height[j])
        
        water = 0
        for i,h in enumerate(height): 
            water += max(min(max_left_vect[i],max_right_vect[i])-h,0)
        
        return water       
        
        
        
        
        
        
        
        
        