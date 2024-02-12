class Solution:
    def majorityElement(self, nums: List[int]) -> int:
#         appears = {}
#         #size = len(nums)
#         max_appears = 0
#         key_max_appears = 0
#         for elem in nums:
#             if elem in appears:
#                 appears[elem] +=1
#             else:
#                 appears[elem] =1
            
#             if  appears[elem] > max_appears:
#                 max_appears = appears[elem]
#                 key_max_appears = elem
            
#             #if max_appears>size/2:
#             #    break
#         return key_max_appears
        
    
        # space = O(1) , time (n)
        cont = 0 
        for num in nums:
            if cont == 0 :
                value = num
            cont += 1 if value == num else -1
        
        return value
      

            

        