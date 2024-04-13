class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
#         # brute force: 
#         def maxAreaColum(i):
#             h = heights[i]
#             n = 1
            
#             #checkleft
#             j = i
#             while j > 0:
#                 j -= 1
#                 if  heights[j] >= h:
#                     n +=1
#                 else:
#                     break
            
#             #check_right:
#             j = i 
#             while j < len(heights)-1:
#                 j +=1 
#                 if  heights[j] >= h:
#                     n +=1
#                 else:
#                     break        
            
#             return n*h
        
#         ans = 0
#         for i in range(len(heights)):
#             ans = max(ans,maxAreaColum(i) )
        
#         return ans





#         def find_leftLimits(heights):
#             stack = []
#             left = []
#             for i,h in enumerate(heights):
#                 print(i,h,"stack:",stack,", left: ",left)
#                 if stack:
#                     while stack: 
#                         if h < heights[stack[-1]]:
#                             stack.pop()
#                         else:
#                             left.append(stack[-1]+1)
#                             stack.append(i)
#                             break

#                 if not stack:
#                     left.append(0)
#                     stack.append(i)
#             print(left)
#             return left
                    
            
#         left = find_leftLimits(heights)

        
#         mod_right = find_leftLimits(heights[::-1])
#         right = [len(heights)-1 - i for i in mod_right[::-1]]
    
        
#         max_area = 0
#         for i,h in enumerate(heights):
#             area = h*(right[i]-left[i]+1)
#             print(i,area)
#             max_area = max(max_area,area)
        
        
#         return max_area
#  NO SE POR QUE NO FUNCIONA PARA  [1,1] @$^#&$^*^*%^&$#^$%^##%@#$#@@#



            maxArea = 0
            stack = [] # pair: (index, height)

            for i, h in enumerate(heights):
                start =i
                while stack and stack[-1][1] > h:
                    index, height = stack.pop()
                    maxArea = max(maxArea, height * (i - index))
                    start = index
                stack.append((start, h))

            for i, h in stack:
                maxArea = max(maxArea, h * (len(heights) - i))
            
            return maxArea














            
            
        