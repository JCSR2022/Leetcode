class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        

        ans = []
        curr_hash = {}
        for w in words:
            w_hash = Counter(w)
            if curr_hash != w_hash:
                ans.append(w)
                curr_hash = w_hash
        
        return ans
        