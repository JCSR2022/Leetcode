class Solution:
    def countSubstrings(self, s: str) -> int:
#         ans = []
#         for i in range(len(s)):
#             for j in range(i):
#                 if s[j:i+1] == s[j:i+1][::-1]:
#                     ans.append(s[j:i+1])
#         L_ans = len(list(s)) + len(ans)
        
#         return L_ans


#   O(n**3) sol
#         ans = 0
#         for i in range(len(s)):
#             for j in range(i):
#                 if s[j:i+1] == s[j:i+1][::-1]:
#                     ans += 1
#         L_ans = len(list(s)) + ans
#         return L_ans     
    
    
#    O(n**2) sol:

        res = 0
    
        def check_palindrom(l,r,res):
            while l >=0 and r < len(s) and s[l] == s[r]:
                res +=1
                l -=1
                r +=1
            return res
    
        for i in range(len(s)):
            #odd substrings
            l = r = i
            res = check_palindrom(l,r,res)
            
            #even substrings
            l = i
            r = i+1
            res = check_palindrom(l,r,res)
        
        return res
            
                
    

