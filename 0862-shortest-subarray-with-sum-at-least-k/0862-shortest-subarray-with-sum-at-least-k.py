class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        #brute force, will not work ime Limit Exceeded:
#         min_size = 10**9+1
        
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 arr = nums[i:j+1]
#                 if sum(arr)>=k:
#                     min_size = min(min_size,len(arr))
                    
#         return min_size if min_size < 10**9 + 1 else -1


#-----------------------------------------------------------

        #sliding window
        # l = 0 , r = 1 , if nums[l,r] >k make window bigger 
#do not work        
#---------------------------------------------------------------        
    
    #using a heap
    
#         ans = float("inf")
#         cur_sum = 0
#         min_heap = [] #(prefix_sum, end_idx)
    
#         for r in range(len(nums)):
#             cur_sum = nums[r]
            
#             if cur_sum >= k:
#                 ans = min(ans,r+1)
                
#             while min_heap and cur_sum - min_heap[0][0] >= k :
#                 prefix, end_idx = heapq.heappop(min_heap)
#                 ans = min(ans,r - end_idx)
            
#             heapq.heappush(min_heap,(cur_sum,r))

#         return -1 if ans == float("inf") else ans
    
    
#------------------------------------------------------------------------

        n = len(nums)
        prefix_sum = [0] * (n + 1)  # Prefix sum array
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        # Monotonic deque to store indices of prefix_sum
        dq = deque()
        result = float('inf')  # Initialize with infinity

        for i in range(n + 1):
            # Check if any subarray satisfies the condition
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                result = min(result, i - dq.popleft())

            # Maintain increasing order in the deque
            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()

            dq.append(i)

        return result if result != float('inf') else -1
    