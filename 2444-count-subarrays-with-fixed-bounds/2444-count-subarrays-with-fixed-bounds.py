class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
# again Brute force:----------------------------------------------
#         cont = 0
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 print(nums[i:j+1],min(nums[i:j+1]) == minK and max(nums[i:j+1]) == maxK  )
#                 if min(nums[i:j+1]) == minK and max(nums[i:j+1]) == maxK:
#                     cont +=1
#         return cont
    
    
# crazy idea------------------------------------------------------

#           cont = 0
#         complete = False
#         processing = False
#         min_num = None
#         max_num = None
                

#         for n in nums:
#             print(n,min_num,max_num,processing,complete,cont)
#             if n > maxK or n < minK:
#                 complete = False
#                 processing = False
#                 min_num = None
#                 max_num = None
#                 continue
            
#             if  not complete and not processing:
#                 if n in [minK,maxK]:
#                     processing = True
#                     if n == minK: min_num = minK 
#                     else: max_num = maxK
#                 continue
            
#             if not complete and processing:
#                 if n in [minK,maxK]:
#                     if n == minK:
#                         if min_num == None:
#                             min_num = n
#                             complete = True
#                             processing = False
        
#                     if n == maxK:
#                         if max_num == None:
#                             max_num = n
#                             complete = True
#                             processing = False
                
                            
#             if  complete and not processing:
#                 cont +=1
                
#         return cont
                
        res = 0
        
        bad_idx = -1
        left_idx = -1
        right_idx = -1
        
        for i,num in enumerate(nums):
            if not minK <= num <= maxK:
                bad_idx = i
                
            if num == minK:
                left_idx = i
                
            if num == maxK:
                right_idx = i
                
            res += max(0, min(left_idx,right_idx)-bad_idx)
                

        return res 
        
        
        
        
# # sliding window:------------------------------------------------------
# #  move left and right until found a min o max
# #  if found fix L until found the complement 
# #   count +=1 if found and quep adding until found 
# #     a valu less than min or grater than max
# #    if found L and R position on that value

#         left = 0
#         cont =0
        
#         for right in range(len(nums)):
#             if ( (max(nums[left:right+1]) == maxK) and 
#                  (min(nums[left:right+1]) == minK)    ):
#                 cont += 1
                
            
                
        
#         return cont
        
  

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
    
    
            