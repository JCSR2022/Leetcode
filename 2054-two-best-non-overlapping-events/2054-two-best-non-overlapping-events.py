from collections import deque
from collections import defaultdict
import bisect
 
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        #https://www.youtube.com/watch?v=gdBsvEOeYho
        timeline = []
        
        for start,end,val in events:
            timeline.append([start,True,val])
            timeline.append([end+1,False,val])
            
        timeline.sort()
        #print(timeline)
        max_val = 0
        max_sean = 0
        for time,start_end,val in timeline:
            if start_end:
                max_val = max(max_val,max_sean+val)
            else:
                max_sean = max(max_sean,val)
            #print(time,start_end,val,max_val,max_sean)
        
        
        return max_val
        
        
#----------------------------------------------
        
#         #aproach
#         #create adjacence matrix with times and edge values, find max path
        
#         adj_mat = {}
#         for start,end,val in events:
#             if start in adj_mat:
#                 adj_mat[start-1].append((val, end))
#             else:
#                 adj_mat[start-1] = [(val, end)]
#             if end not in adj_mat:
#                 adj_mat[end] = []
                
        
#         def find_max_path(adj_mat):
            
#             start = min(adj_mat.keys())
#             visited = set()
#             max_path = 0
#             q = deque((0,start))
            
#             while q:
#                 path_val,node = q.popleft()
# noooo, ni siqueira entendiste el problema, son dos no overlapping!!           #--------------------------------------------------------------------     


































#         n = len(events)
        
#         # Step 1: Sort the events by their start time
#         events.sort(key=lambda x: x[0])
        
#         # Step 2: Create the suffix array for the maximum event value from each event onward
#         suffixMax = [0] * n
#         suffixMax[n - 1] = events[n - 1][2]  # Initialize the last event's value
        
#         # Populate the suffixMax array
#         for i in range(n - 2, -1, -1):
#             suffixMax[i] = max(events[i][2], suffixMax[i + 1])
        
#         # Step 3: For each event, find the next event that starts after it ends
#         maxSum = 0
        
#         for i in range(n):
#             left, right = i + 1, n - 1
#             nextEventIndex = -1
            
#             # Perform binary search to find the next non-overlapping event
#             while left <= right:
#                 mid = left + (right - left) // 2
#                 if events[mid][0] > events[i][1]:
#                     nextEventIndex = mid
#                     right = mid - 1
#                 else:
#                     left = mid + 1
            
#             # If a valid next event is found, update the max sum
#             if nextEventIndex != -1:
#                 maxSum = max(maxSum, events[i][2] + suffixMax[nextEventIndex])
            
#             # Also consider the case where we take only the current event
#             maxSum = max(maxSum, events[i][2])
        
#         return maxSum           
            
            
   
        