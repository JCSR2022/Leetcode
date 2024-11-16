class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        #brute force: o(n*(n-k)) O(n**2)
        
#         def isAscendingConsecutive(arr):
#             if len(arr) <= 1:
#                 return True
            
#             for i in range(len(arr)-1):
#                 if arr[i] >= arr[i+1]:
#                     return False
#                 if arr[i]+1 != arr[i+1]:
#                     return False
            
#             return True
        
#         ans =[]
#         for i in range(len(nums)-k+1):
#             arr = nums[i:i+k]
#             if isAscendingConsecutive(arr):
#                 ans.append(max(arr))
#             else:
#                 ans.append(-1)
        
#         return ans
        

#---------------------------------------------------    
    
        #sliding window (An-Wen Deng)
        
        n=len(nums)
        if n==1 or k==1: return nums
        ans=[-1]*(n-k+1)
        Len=1
        for r in range(1, n):
            Len=Len+1 if nums[r]==nums[r-1]+1 else 1
            if Len>=k: ans[r-k+1]=nums[r]
        return ans
        