class Solution:
    def minDifference(self, nums: List[int]) -> int:
    
    
        if len(nums) <= 4:
            return 0
        nums.sort()
        ans = nums[-1] - nums[0]
        for i in range(4):
            ans = min(ans, nums[-(4 - i)] - nums[i])
        return ans
    
#         if len(nums) <= 4:
#             return 0 
#         else:
#             temp = []
#             for _ in range(2):
#                 min_value = min(nums)
#                 temp.append(min_value)
#                 nums.remove(min_value)
#             min_value = min(nums)
#             temp.append(min_value)
            
#             for _ in range(3):
#                 max_value = max(nums)
#                 temp.append(max_value )
#                 nums.remove(max_value)
#             temp.sort()
            
#             print(temp)
            
#             ans = [] 6-4+i     i +2
#             for i in range(4):
#                 ans.append(temp[i-4]-temp[i] )
                
#                 print(i,i-4,temp[i-4],temp[i],ans)
            
#             return min(ans)
    
    
    
#         # special cases nums.legth < 4..
#         if len(nums) <= 4:
#             return 0 
        
#         if len(nums) == 5:
#             nums.sort()
#             print(nums)
#             if nums[2]-nums[1]>nums[3]-nums[2]:
#                 return nums[3]-nums[2]
#             else:
#                 return nums[2]-nums[1]
            
#         if len(nums) >= 6:
#             min_value = min(nums)
#             max_value = max(nums)
#             nums.remove(min_value)
#             nums.remove(max_value)
            
#             temp = []
#             min_value = min(nums)
#             temp.append(min_value)
#             nums.remove(min_value)
#             min_value = min(nums)
#             temp.append(min_value)
#             nums.remove(min_value)

#             max_value = max(nums)
#             temp.append(max_value )
#             nums.remove(max_value)
#             max_value = max(nums)
#             temp.append(max_value)
#             nums.remove(max_value)
#             print(temp)
#             if temp[1]-temp[0] > temp[2]-temp[3]:
#                 return temp[2]-temp[1]
#             else:
#                 return temp[3]-temp[0]

        