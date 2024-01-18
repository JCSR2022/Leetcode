class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        size_s = len(s)
        if size_s == 0:
            return True
        
        j = 0 
        for letter in  t:
            if s[j] == letter:
                j +=1 
                if j == size_s:
                    return True
        return False
        