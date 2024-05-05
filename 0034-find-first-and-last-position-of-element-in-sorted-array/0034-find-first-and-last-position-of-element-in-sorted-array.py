class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # aproach 
        # first binary search
        # second find window
        
        
        
        def binarySearch(nums,target):
            l = 0
            r = len(nums)-1
            
            while l <= r:
                
                m =  l + (r-l)//2
                
                #print((l,r,m),nums[l],nums[r],nums[m])
                
                if nums[m] == target:
                    return m
                
                if target < nums[m] :
                    r = m-1
                
                if target > nums[m] :
                    l = m+1
                    
            return -1
            
          
        inicial_index =  binarySearch(nums,target)
        #print(inicial_index)  
        
        
        # find window
        if inicial_index == -1:
            return [-1,-1]
        
        l = inicial_index
        r = inicial_index
        
        while l > 0 and nums[l-1] == target:
            l -= 1
        while r < len(nums)-1  and nums[r+1] == target:
            r += 1
            
        return [l,r]
            
        
        
        
        
        
        