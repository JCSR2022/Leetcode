class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        
        # https://www.youtube.com/watch?v=Fv3M9uO5ovU
        
        q = deque()
        res = 0
        
        for i in range(len(nums)):
            while q and i > q[0] + k -1:
                q.popleft()
            
            if (nums[i]+len(q)) % 2 == 0:
                if i + k > len(nums):
                    return -1
                res +=1
                q.append(i)
                
        return res
        
        
        
     
        
        
        
        
        
        
        
        
        #1. start window at 0, has to be size k
        #2. flip, dome might turn into 0
        #3. start window there
        
#         cur_window_flips = 0
#         res = 0
#         for i in range(len(nums)):
#             if i-k >= 0 and nums[i-k] == 2:
#                 cur_window_flips -= 1
            
#             if (cur_window_flips + nums[i]) %2 == 0:
#                 if i + k > len(nums):
#                     return -1
#                 nums[i] = 2
#                 cur_window_flips +=1
#                 res += 2
                
#         return res
        
        
        