class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
         
        cur_min = arrays[0][0]
        cur_max = arrays[0][-1]
        
        ans = float("-inf")
        
        for arr in arrays[1:]:
            ans = max(ans,arr[-1]-cur_min,cur_max-arr[0])            
            cur_min = min(cur_min,arr[0])
            cur_max = max(cur_max,arr[-1])
            
        return ans     
            
            
#         #!@@%^#$^#Y%$&$%^&%*^&*%^*(%^(%&#%!@#R!@$!@!))
#         min_val_1 = [arrays[1][0],1]
#         max_val_1 = [arrays[0][-1],0]
        
#         min_val_2 = [arrays[0][0],0]
#         max_val_2 = [arrays[1][-1],1]
        
#         print(max_val_2, min_val_2,max_val_1 ,min_val_1)
#         if len(arrays) == 2:
#             return max(abs(max_val_2[0]-min_val_1[0]), abs(max_val_1[0]-min_val_2[0])) 
        
#         for i in range(2,len(arrays)):
            
#             if arrays[i][0] < min_val_2[0]:
#                 min_val_1 = min_val_2 
#                 min_val_2 = [arrays[i][0],i]
                
#             if arrays[i][-1] > max_val_2[0]:
#                 max_val_1 = max_val_2
#                 max_val_2 = [arrays[i][-1],i]
   


#         if min_val_2[1] != max_val_2[1]:
#             return abs(max_val_2[0]-min_val_2[0])
        
#         else:
#             return max(abs(max_val_2[0]-min_val_1[0]), abs(max_val_1[0]-min_val_2[0]))

        
      