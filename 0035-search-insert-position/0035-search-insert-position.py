class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # divide and conquer 
        
#         def divConq(arr,index=0):
#             if arr:
                
#                 if len(arr) == 1:
#                     if arr[0]  >= target:
#                         return index
#                     else:
#                         return index + 1

#                 elif len(arr) > 1:
#                     index = len(arr)//2
#                     arrL = arr[:index]
#                     arrR = arr[index+1:]
#           NOOOOOOOOOOOOOOOOOOOOOO

        #binary search
    
    
        L = 0
        R = len(nums) - 1
        
        while L <= R:
            
            mid = (L+R)//2
            
            if target == nums[mid]:
                return mid
            
            if target > nums[mid]:
                L = mid + 1
            else:
                R = mid - 1
        
        
        return L
            
        
        
        


                
                
                
                
            
            
        return divConq(nums)
        
                



     
    
    
    
        return 0