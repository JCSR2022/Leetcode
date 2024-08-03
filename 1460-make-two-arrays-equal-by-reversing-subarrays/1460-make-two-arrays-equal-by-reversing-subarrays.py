class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        #if set target == set arr 
        
        c_arr = Counter(arr)
        c_target = Counter(target)
        
        return c_target==c_arr
        