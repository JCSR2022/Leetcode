class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        
        
#         # aproach sliding window cheking curret max and global max
        
#         # ord(caracter)  a =97 z =122
        
#         def check_adjacent(caracter_1,caracter,k):
#             return abs(ord(caracter)- caracter_1) <= k
        
#         l = 0
#         r = 0
#         gs = s[l] # global_subsequence
#         cs = s[l] # current_subsequence
        
#         while r < len(s):
#             r += 1
#             if check_adjacent(s[r-1],s[r],k):   # is not s[r-1] but the previus charactes
#                 cs
                
#---------------------------------------------------------------------------------
        
        
#         # brute force recursive solution
        
        
#         cache = {}
        
#         def helper(i,prev):
#             if i == len(s):
#                 return 0
            
#             if (i,prev)  in cache:
#                 return cache[(i,prev)]
            
#             res = helper(i+1,prev)
            
#             if prev == "" or  abs(ord(s[i])-ord(prev)) <= k:
#                 res= max(res,1+ helper(i+1,s[i]))
        
#             cache[(i,prev)] = res
            
#             return res
        
#         return helper(0,'')
    

    
#---------------------------------------------------------------------------------
        
       
        # dinamic programing !!!   
        
        
        dp = [0] * 26  # a-z
        
        for c in s:
            curr = ord(c)-ord('a')
            longest = 1
            for prev in range(26):
                if abs(curr-prev) <=k:
                    longest = max(longest,1+dp[prev])
                    
            dp[curr] = max(dp[curr],longest)
                
        return max(dp)
    
        
        
        
        
        
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
        
        
        
        
        