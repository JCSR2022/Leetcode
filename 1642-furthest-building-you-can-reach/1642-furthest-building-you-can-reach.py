class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        N = len(heights)
        heap = []
        
        for i in range(N-1):
            h = heights[i+1] - heights[i]
            if h <= 0 : continue
            heappush(heap,h)
            if len(heap)>ladders:
                min_h   = heappop(heap)
                bricks -= min_h
            if bricks < 0 : return i
        
        return N-1
                
        
        
        
#         actual_high = heights[0]
        
#         if ladders == 0:
#             for i,next_high in enumerate(heights):
#                 if i > 0:
#                     jump = next_high - actual_high 
#                     if jump <= 0:
#                         actual_high = next_high 
#                         continue
#                     else:
#                         if bricks - jump >= 0:
#                             bricks -=jump
#                             actual_high = next_high 
#                         else:
#                             return i   
                                                
#         return i

            
#                                 [bricks=b,ladders=l]
#                         if b > actual_high   if l > 0
#                                /                 \
#                 [bricks=b-h1,ladders=l]         [bricks=b,ladders=l-1]                
#         if b > actual_high    if l > 0
#                /                 \
# [bricks=b-h1-h2,ladders=l]         [bricks=b-h1,ladders=l-1]  
#      ...............       
# if b < actual_high,if l == 0          



        
        
    
    
    
    
    
    
        
        
        
        
        