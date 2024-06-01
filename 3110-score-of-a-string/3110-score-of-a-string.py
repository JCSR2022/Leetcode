class Solution:
    def scoreOfString(self, s: str) -> int:
        
        # burte force:
        
        ans = 0
        
        s_list = [ ord(k) for k in s]
        
        for i in range(1,len(s)):
            ans += abs(s_list[i-1]-s_list[i])    
    
        return ans
        