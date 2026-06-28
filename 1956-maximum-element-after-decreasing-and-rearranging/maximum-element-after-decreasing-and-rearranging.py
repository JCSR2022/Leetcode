class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        #brute force like you
        
        arr.sort()
        curr_max = 0
        for n in arr:
            if n > curr_max:
                curr_max +=1
            
        return curr_max