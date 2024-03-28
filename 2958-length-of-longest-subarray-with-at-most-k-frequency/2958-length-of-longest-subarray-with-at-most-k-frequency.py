class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        # sliding window:
        # ponters l and r , cont and maxCont = 
        # move pointers while r < len(nums) 
        # create a hashtable:
        #     maxFrec of nums[r] in hash table
        #     while maxFrec < k:
        #        r += 1 , cont +=1 , maxCont = max(maxCont,cont)
        #        push nums[r] in hashtable
        #     while maxFrec > k:
        #        l += 1 , cont -=1 
        #        pop nums[l] from hastable
        
        
        def pushHashTable(n):
            if n in hashtable:
                hashtable[n] += 1
            else:
                hashtable[n] = 1
                
        def isMaxfrec(n):
            if hashtable[n] > k:
                return True
            else:
                return False
            
        def popHashTable(n):
            hashtable[n] -= 1
        
        l = 0
        r = 1
        
        cont = 1 
        maxCont = 1
        hashtable = {nums[0]:1}
        
        while r < len(nums):
            pushHashTable(nums[r])
            while isMaxfrec(nums[r]):
                popHashTable(nums[l])
                l += 1
                cont -=1
            cont +=1
            maxCont = max(maxCont,cont)
            r +=1
            
            
        return maxCont
            
        
        
        