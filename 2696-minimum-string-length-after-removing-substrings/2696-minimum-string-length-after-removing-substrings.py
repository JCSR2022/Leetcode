class Solution:
    def minLength(self, s: str) -> int:
        # O(n) using a queue
        
        if len(s) == 1:
            return 1
        
        ans = ""
        for ch in s:
            ans += ch
            if ans[-2:] == 'AB':
                ans = ans[:-2]
            if ans[-2:] == 'CD':
                ans = ans[:-2]
                
        return len(ans)
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        #brute force:
#         while 'AB' in s or 'CD' in s:
#             while 'AB' in s:
#                 s = s.replace("AB", "")
#             while 'CD' in s:
#                 s = s.replace("CD", "")
        
#         return len(s)
        