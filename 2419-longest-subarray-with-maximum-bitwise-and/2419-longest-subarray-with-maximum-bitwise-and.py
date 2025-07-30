class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        #aproach , find the max window with the max value??

        max_size = 1
        max_value = 0
        for n in nums:
            if n > max_value:
                max_value = n 
                curr_size = 1
                max_size = 1
            elif n == max_value:
                curr_size +=1
                max_size =max(max_size,curr_size) 
            else:
                curr_size = 0
            

        return max_size 




        return 2




















#---------------------------------------------------------
#brute force O(n**2):
#         result = 0
#         max_and = 0
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 actual = nums[i:j+1]
#                 actual_and = functools.reduce(lambda x, y: x & y, actual )
#                 if actual_and ==  max_and:
#                     result = max(len(actual),result)
#                 elif actual_and >  max_and:
#                     max_and = actual_and
#                     result = len(actual)
#                 #print(actual,actual_and,max_and,result)   
#         return result




        #liniar aproach:
        #find max bit rep num and index
        #count elements continuos iqual to max
        
        
#         max_bits = 0
#         pre_ans = (0,0) # number with max bits, index
#         for i,elem in enumerate(nums):
#             print(i,elem,bin(elem).count('1'),max_bits,pre_ans )
#             num_bits = bin(elem).count('1')
#             if num_bits > max_bits:
#                 max_bits = num_bits
#                 pre_ans = (elem,i)
        
#         print(i,elem,bin(elem).count('1'),max_bits,pre_ans )
#         print(max_bits,pre_ans)
        
#         ans = 1
#         i = pre_ans[1]+1
#         num = pre_ans[0]
#         while i < len(nums) and nums[i] == num:
#                 i += 1
#                 ans +=1
                
#         return ans
                
#-------------------------------------------------------------    
        # # Time O(2*n) 
        # ans = 0
        # cont = 0
        # max_num = max(nums)
        
        # for num in nums:
        #     if num == max_num:
        #         cont += 1
        #         ans = max(ans,cont)
        #     else:
        #         cont = 0
        # return ans
                
        
        
            