class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        def helper(i,count):
            """
            count is a hashmap, lib
            """
            if i == len(nums):
                return 1
            
            res  = helper(i+1, count) # skip nums[i]
            
            if not count[nums[i]+k] and not count[nums[i] - k]:
                count[nums[i]] += 1
                res += helper(i+1,count)
                count[nums[i]] -= 1
            return res
        
        
        return helper(0,defaultdict(int)) - 1
                
  









        
#         def mycombinations(iterable, r):
#             # combinations('ABCD', 2) → AB AC AD BC BD CD
#             # combinations(range(4), 3) → 012 013 023 123
        
#             pool = tuple(iterable)
#             n = len(pool)
        
#             if r > n:
#                 return
#             indices = list(range(r))
#             yield tuple(pool[i] for i in indices)
#             while True:
#                 for i in reversed(range(r)):
#                     if indices[i] != i + n - r:
#                         break
#                 else:
#                     return
#                 indices[i] += 1
#                 for j in range(i+1, r):
#                     indices[j] = indices[j-1] + 1
#                 yield tuple(pool[i] for i in indices)
        
#         for i in range(len(nums)+1):
#             ans = [x for x in mycombinations(nums, i)]
#             print(ans)
        
#         return 4

        



        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        