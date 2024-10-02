class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        #brute force
        
        #hash_arr = {num:i+1 for i,num in enumerate(sorted(set(arr)))}
        #return [hash_arr[n] for n in arr]
        
        
        if not arr: return []
            
        new_arr = list(set(arr))
        heapq.heapify(new_arr)
        
        cont = 1
        val = heapq.heappop(new_arr)
        hash_arr = {val:cont}
        while new_arr:
            new_val = heapq.heappop(new_arr)
            if new_val != val:
                cont +=1
                hash_arr[new_val] = cont
                val = new_val
            
        return [hash_arr[n] for n in arr]
    
    
    
    
    
    
        