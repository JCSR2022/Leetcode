class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        #brute force
        
        hash_arr = {num:i+1 for i,num in enumerate(sorted(set(arr)))}
        return [hash_arr[n] for n in arr]
        
        #return [{num:i+1 for i,num in enumerate(sorted(set(arr)))}[n] for n in arr]