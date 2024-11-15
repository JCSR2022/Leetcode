class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
#         N = len(arr)
        
#         if N == 1:
#             return 0
        
#         #find postfix
#         l = 0 
#         while l <= N and arr[l+1] >= arr[l]:
#             l +=1
#         ans = N-1-l
        
        
#         #find prefix
#         r = N-1
#         while r> 0 and arr[r-1] <= arr[r]:
#             r -=1
#         ans = min (ans,r)
        
        
#         #find middle
#         l = 0
#         r = N-1
#         while l <= r:
            
#             while r< N and l + 1 < r and arr[r-1] <= arr[r] and arr[l] <= arr[r]:
#                 r -= 1
                
#             while r < N and arr[l] > arr[r]:
#                 r += 1
                
#             ans = min(ans,r-l-1)
            
#             if arr[l] > arr[l+1]:
#                 break
                
#                 l += 1
        
        
#         return ans



        n = len(arr)
        
        # Step 1: Find the longest non-decreasing prefix
        left = 0
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1
        
        # If the entire array is non-decreasing
        if left == n - 1:
            return 0
        
        # Step 2: Find the longest non-decreasing suffix
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        
        # Step 3: The minimum elements to remove is the minimum of:
        # 1. Removing all elements from right of 'left' or left of 'right'
        result = min(n - left - 1, right)
        
        # Step 4: Try to merge the prefix and suffix by checking if we can connect arr[left] and arr[right]
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1
        
        return result