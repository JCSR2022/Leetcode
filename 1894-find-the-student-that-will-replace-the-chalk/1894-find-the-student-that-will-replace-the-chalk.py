class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        new_k = k%sum(chalk)
        
        for i,n in enumerate(chalk):
            new_k -= n
            if new_k < 0:
                return i