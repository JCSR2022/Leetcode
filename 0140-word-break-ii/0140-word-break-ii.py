class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        #to reduce time
        wordDict = set(wordDict)
        
        
        def backtrack(i):
            if i == len(s):
                res.append(" ".join(cur))
                return 
            
            for j in range(i,len(s)):
                w = s[i:j+1]
                if w in wordDict:
                    cur.append(w)
                    backtrack(j+1)
                    cur.pop()
                    
        cur = []
        res = []
        
        backtrack(0)
        
        return res
        
        
        
        
#         ans = ""
#         i = 0
#         word = ""
#         while i < len(s):
#             word += s[i]
            
#             if word in wordDict:
#                 ans += word + ' '
#                 word = ''
#             i += 1        
#         return [ans]

    #--------------------------------------
        
#         def backtrack(i,res):
#             if i >= len(s):
#                 return
            
#             ans = backtrack(i+1)
            
#             if ans: 
#                 res.append(ans)
                
                
            
            
        