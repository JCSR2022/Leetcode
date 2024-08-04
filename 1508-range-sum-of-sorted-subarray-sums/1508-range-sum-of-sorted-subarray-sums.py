class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        mode = 10**9+7
        
#         #REEEEBrute force
#         arr = []
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)+1):
#                 arr.append(sum(nums[i:j])%mode)
#         arr.sort()
        
#         return sum(arr[left-1:right])%mode

    
        arr = []
        for i in range(n):
            current_sum = 0
            for j in range(i,n):
                current_sum += nums[j]
                arr.append(current_sum)
        arr.sort()
        
        return sum(arr[left-1:right])%mode
         