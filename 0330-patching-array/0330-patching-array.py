from itertools import combinations

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        
        miss, added, index = 1, 0, 0
        while miss <= n:
            if index < len(nums) and nums[index] <= miss:
                miss += nums[index]
                index += 1
            else:
                miss += miss
                added += 1
        return added
        
        
        
        
        
        # scund aproach
        # calculate all posible sums with nums  , conver to set allPosSum
        # find min value to add,   add to allPosSum and extend allPosSum
        # check if allPosSum == range(n+1)
        
        
#         def is_allPosSum_rangeN(allPosSum):
#             for i in range(1,n+1):
#                 if i not in allPosSum:
#                     return False
#             return True
            
            
#         def findMinPatch(arr):
#             arr_sorted = sorted(arr)
#             smallest_missing = 1
            
#             for num in arr_sorted:
#                 if num <= smallest_missing:
#                     smallest_missing += 1
#                 elif num > smallest_missing:
#                     break
#             return  smallest_missing      
        
        
#         # icicial allPosSum
#         all_combinations = []
#         for r in range(1, len(nums) + 1):
#             all_combinations.extend(combinations(nums, r))
#         allPosSum = set([ sum(n) for n in all_combinations])
        
#         k = 0
#         print(k,allPosSum,is_allPosSum_rangeN(allPosSum))
#         print()
        
#         while not is_allPosSum_rangeN(allPosSum):
#             k +=1
            
#             newNum = findMinPatch(list(allPosSum))
#             nums.append(newNum)
#             nums.sort()
#             print(nums)
            
#             newPosSum = [i+newNum for i in allPosSum ]
#             for i in newPosSum: allPosSum.add(i)
#             allPosSum.add(newNum)
            
#             print(k,allPosSum,is_allPosSum_rangeN(allPosSum))        
#             print()
    
#         return  k        
        
        
        
        
        
        #Brute force do not work Memory Limit Exceeded
#         def isAllPosSum(nums,n):
#             # Generate all possible non-empty combinations
#             all_combinations = []
#             for r in range(1, len(nums) + 1):
#                 all_combinations.extend(combinations(nums, r))
#             all_sums = set([ sum(n) for n in all_combinations])
#             #print(all_combinations)
#             #print(list(all_sums))
#             for i in range(1,n+1):
#                 if i not in all_sums:
#                     return False
#             return True
        
        

#         def include_min_missing(arr):
#             # Sort the array
#             arr_sorted = sorted(arr)
#             # Start checking from 1
#             smallest_missing = 1

#             # Iterate through the sorted array to find the smallest missing positive integer
#             for num in arr_sorted:
#                 if num == smallest_missing:
#                     smallest_missing += 1
#                 elif num > smallest_missing:
#                     break
#             # Add the smallest missing integer to the array
#             arr.append(smallest_missing)
#             #print(arr)

        
#         k = 0
#         while not isAllPosSum(nums,n):
#             include_min_missing(nums)
#             k += 1
  
#         return k








        
        
        
        


        

        