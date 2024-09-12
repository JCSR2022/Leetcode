class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
#         set_allowed = set(allowed)
        
#         ans = 0
#         for w in words:
#             if set(w).issubset(set_allowed): ans +=1
                
#         return ans

        count = 0
        for i in range(len(words)):
            if sorted(set(list(words[i] + allowed))) == list(sorted(allowed)):             count += 1
        return count

 