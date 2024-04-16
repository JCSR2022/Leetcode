class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        # opcion 1: usar Kadane's Algorithm
#         def MaxWindow(arr):
#             c = arr[0]
#             g = arr[0]
            
#             for i in range(1,len(arr)):
#                 c = max(arr[i],c+arr[i])
#                 g = max(g,c)
            
#             return g
        
        
#         new_nums = nums + nums[:len(nums)-1]
#         #print(new_nums)
        
#         maximo = -inf
#         for i in range(len(new_nums)-len(nums)+1):
#             c_maximo = MaxWindow(new_nums[i:len(nums)+i])
#             maximo = max(maximo,c_maximo)
#             #print(new_nums[i:len(nums)+i],c_maximo,maximo)
#         return maximo
        
        
       # buscando el minimo
    
    
    
        c_max = c_min = nums[0]
        g_max = nums[0]
        g_min = nums[0]
        
        for i in range(1,len(nums)):
            c_max = max(nums[i],c_max+nums[i])
            g_max = max(g_max,c_max)
            
            c_min = min(nums[i],c_min+nums[i])
            g_min = min(g_min,c_min)
            
            
        #print(g_max,g_min,sum(nums), max(g_max,sum(nums)-g_min ))
        if g_max > 0:
            return max(g_max,sum(nums)-g_min )
        else:
            return g_max
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        # opcion 2 , modificar   Kadane's Algorithm      
        

#         arr = nums + nums
        
#         w = [0]*len(nums)
#         w[-1] = arr[0]
        
#         g = arr[0]
#         max_arr = []
#         print(arr)
#         for i in range(1,len(arr)):
#             print(w,sum(w),arr[i],arr[i] > sum(w)+arr[i],g)
            
#             if arr[i] > sum(w) +arr[i]:
#                 w = [0]*len(nums)
#                 w[-1] = arr[i]
#             else:
#                 w.pop(0)
#                 w.append(arr[i])
    
                
#             if sum(w) > g :
#                 g = sum(w)
#                 max_arr = w.copy()
        
#         print(max_arr)
#         return g
        
           
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         n = len(nums)
        
#         current_indexs = [0,0]
#         global_indexs = [0,0]
        
#         global_max = nums[0]
#         current_max = nums[0]
        
#         for i in range(1,n):
#             if current_max + nums[i] > nums[i]:
#                 current_max = current_max + nums[i]
#                 current_indexs[1] = i 
#             else:
#                 current_max = nums[i]
#                 current_indexs[0] = i 
#                 current_indexs[0] = i 
#             if  current_max > global_max :   
#                 global_max = current_max
#                 global_indexs = current_indexs
                
      
        
#         left = global_indexs[0]
#         right_current_indexs = [0,0]
#         right_global_indexs = [0,0]
        
#         for j,num in enumerate(nums):
#             if j > left:
#                 return global_max
#             else:
#                 if current_max + num > num:
#                     current_max = current_max + num
#                     right_current_indexs[1] = j 
#                 else:
#                     current_max = num
#                     right_current_indexs[0] = j 
#                     right_current_indexs[0] = j 
                    
#                 if  current_max > global_max :   
#                     global_max = current_max
#                     right_global_indexs = right_current_indexs                  
                   

#         return global_max
                        
            
            