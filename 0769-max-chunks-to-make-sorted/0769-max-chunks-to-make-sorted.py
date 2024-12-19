class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        max_sean = float("-inf")
        count_grups = 0
        
        for i,n in enumerate(arr):
            max_sean = max(max_sean,n)
            if max_sean == i:
                max_sean = float("-inf")
                count_grups +=1
        
        return count_grups