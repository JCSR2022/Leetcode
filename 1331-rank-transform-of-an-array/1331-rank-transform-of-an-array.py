class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        #brute force
        
        #hash_arr = {num:i+1 for i,num in enumerate(sorted(set(arr)))}
        #return [hash_arr[n] for n in arr]
        
        
        #-------------------------------------------------------
        
        if not arr: return []

        new_arr = arr.copy()
        heapq.heapify(new_arr)
        
        cont = 0
        hash_arr = {}
        while new_arr:
            val = heapq.heappop(new_arr)
            if val not in hash_arr:
                cont += 1
                hash_arr[val] = cont
              
        return [hash_arr[n] for n in arr]
    
    
    
    
    
    
        