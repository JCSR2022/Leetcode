class Solution:
    def jump(self, nums: List[int]) -> int:
        size = len(nums)
        jumps = 0
        min_window_jump = 0
        max_window_jump = 0
        
        while max_window_jump < size - 1:
            #print(jumps,nums[min_window_jump:max_window_jump+1])
            max_jump = 0 
            for i in range(min_window_jump,max_window_jump+1):
                max_jump = max(max_jump, i + nums[i])
            min_window_jump = max_window_jump + 1
            max_window_jump = max_jump
            jumps +=1
            
        return jumps