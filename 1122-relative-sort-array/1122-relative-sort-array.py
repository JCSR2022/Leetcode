class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        HashMap = {k:0 for k in arr2}
        
        not_in_arr2 = []
        
        for elem in arr1:
            if elem in arr2:
                HashMap[elem] += 1
            else:
                not_in_arr2.append(elem)
        
        not_in_arr2.sort()
        
        in_arr1 = []
        for k,n in HashMap.items():
            for _ in range(n):
                in_arr1.append(k) 
    
        return in_arr1 + not_in_arr2
        