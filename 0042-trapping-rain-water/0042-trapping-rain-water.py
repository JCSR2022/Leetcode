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
                
    
            
        
        
        
        
        
        
        #aproach 2: two pointers
        # p1 : find a peak if found move p2 until find a peak
        # if p2 >= p1 calculate the water between p1 and p2:
        #   calulateWater = for i in range(p1,p2)    sum( min(h[p1],h[p2]) - h[i])
        #   p1 = p2 continue finding new p2
        # if p2 > lengt(height): p1 +=1 and p2 = p1 
        #   until p1 = lengt(height)
        
        
#         def calulateWater(p1,p2):
#             water = 0
#             maxhwater = min(height[p1],height[p2])
#             for i in range(p1+1,p2):
#                 water += max(maxhwater - height[i],0)
#             return water
            
        
#         p1 = -1
#         p2 = 0
#         peak = False
#         water = 0
#         while p1 <= len(height): 
#             if not peak:
#                 p1 += 1 
#                 print(0,(p1,height[p1]),(p2,height[p2]),water)
#                 if p1 >=len(height):
#                     break
                
#                 if height[p1] >= 0:
#                     peak = True
#                     p2 = p1
#                     p1_peak = height[p1]
#             else:
#                 while peak:
#                     #print(1,p1,p2,height[p2] >= height[p1])
#                     p2 +=1 
    
#                     if p2 >= len(height):
#                         peak = False
#                         break
                    
#                     if height[p2] >= height[p1]:
#                         water += calulateWater(p1,p2)
#                         peak = False
#                         p1 = p2-1
#         return water
                    
# -------------------------------------------------------------------
        # aproach 3  pointer and hash table
        # create a hash_peak with {peak: position, } {0:0} ,   p = 0, height[p] =0   {0:0, 1:1, 2:3}  
        #
        #    if height[p] > 0 
        #        if height[p] >= max(hash_peak.keys())
        #               water = calulateWater(hash_peak[max(hash_peak.keys())],p)
        #               del hash_peak[max(hash_peak.keys())]
        #                hash_peak[height[p]] = p 
    
    
        ##p = 0, height[p] =0   min(hash_peak.keys()) = 0
                    
        #           insert into hash_peak {}
        #        else:
        #
        #
        #    else:
        #        p +=1
        #     
        #    
        
        
#         def calulateWater(p1,p2):
#             water = 0
#             maxhwater = min(height[p1],height[p2])
#             for i in range(p1+1,p2):
#                 water += max(maxhwater - height[i],0)
#             return water    
            
# -------------------------------------------------------------------


        def max_left_height(i):
            if i < 1:
                return 0
            return max(height[:i])

        def max_right_height(i):
            if i > len(height)-2:
                return 0
            return max(height[i+1:])

        water = 0
        for i,h in enumerate(height):
            #print(height,i,'max_left:',max_left_height(i) ,'max_right:',max_right_height(i), max(min(max_left_height(i) ,max_right_height(i))-h,0))  
            water += max(min(max_left_height(i) ,max_right_height(i))-h,0)
        
        return water
        
        
        
        