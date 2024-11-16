class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        #brute force:
        
        def isAscendingConsecutive(arr):
            if len(arr) <= 1:
                return True
            
            for i in range(len(arr)-1):
                #print("#",i,arr[i],arr[i+1],arr[i] > arr[i+1])
                if arr[i] >= arr[i+1]:
                    return False
                if arr[i]+1 != arr[i+1]:
                    return False
            
            return True
        
        ans =[]
        for i in range(len(nums)-k+1):
            arr = nums[i:i+k]
            #print(i,arr,isAscending(arr))
            if isAscendingConsecutive(arr):
                ans.append(max(arr))
            else:
                ans.append(-1)
        
        return ans
            
        
        