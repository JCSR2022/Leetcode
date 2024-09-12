class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
#         set_allowed = set(allowed)
        
#         ans = 0
#         for w in words:
#             if set(w).issubset(set_allowed): ans +=1
                
#         return ans

        return sum(set(allowed) >= set(i) for i in words)