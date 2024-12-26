class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        #brute force, try all options:

#         ans = 0
#         expressions = [list(combinacion) for combinacion in product([1, -1], repeat=len(nums))]
        
#         for exp in expressions:
#             if sum([x * y for x, y in zip(nums, exp)]) == target:
#                 ans +=1
                
#         return ans

#Time Limit Exceeded
#-----------------------------------------------------   
#         leaf = []
#         def backtrack(i,cur_sum):
#             print(i, cur_sum, leaf)
#             if i == len(nums):
#                 leaf.append((cur_sum,cur_sum == target))
#                 return 1 if cur_sum == target else 0

#             return ( backtrack(i+1,cur_sum + nums[i] ) + 
#                      backtrack(i+1,cur_sum - nums[i] )   )

#         return backtrack(0,0)
    
    
#Time Limit Exceeded
#----------------------------------------------------- 

# backtrack with memorization 

#         memory = {}

    
#         def backtrack(i,cur_sum):
            
#             if (i,cur_sum) in memory:
#                 return memory[(i,cur_sum)]
    
#             if i == len(nums):
#                 return 1 if cur_sum == target else 0
            
#             memory[(i,cur_sum)] = backtrack(i+1,cur_sum + nums[i] ) + backtrack(i+1,cur_sum - nums[i] )
#             return memory[(i,cur_sum)] 

#         return backtrack(0,0)

#--------------------------------------------------

#https://www.youtube.com/watch?v=dwMOrl85Xes
#dp solution

        dp = [defaultdict(int) for _ in range(len(nums)+1)]
        #dp[ elements of nums, sum of elements]
        
        dp[0][0]  =1 #  1 way to sum to zero with 0 elements
        
        for i in range(len(nums)):
            for cur_sum, count in dp[i].items():
                dp[i+1][cur_sum + nums[i]] += count
                dp[i+1][cur_sum - nums[i]] += count
        
        # for i,level in enumerate(dp):
        #     print(i,{k: level[k] for k in sorted(level)}    )
        
        
        #dp[len(nums)][target] number of ways sum target with all nums
        
        return dp[len(nums)][target]
