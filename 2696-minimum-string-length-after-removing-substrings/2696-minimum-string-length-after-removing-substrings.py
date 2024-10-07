class Solution:
    def minLength(self, s: str) -> int:
        
        
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
                continue
            if c == "B" and stack[-1] == "A":
                stack.pop()
            elif c == "D" and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(c)
        return len(stack)  




#         # O(n) using a queue
#         ans = ""
#         for ch in s:
#             ans += ch
#             print(ans)
#             if ans[-2:] == 'AB':
#                 ans = ans[:-2]
#             if ans[-2:] == 'CD':
#                 ans = ans[:-2]
#         return len(ans)
            
                 
        
        #brute force:
#         while 'AB' in s or 'CD' in s:
#             while 'AB' in s:
#                 s = s.replace("AB", "")
#             while 'CD' in s:
#                 s = s.replace("CD", "")
        
#         return len(s)
        