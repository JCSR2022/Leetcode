class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
#         window =[]
#         maxSize = 0
#         for l in s:
#             if l in window:
#                 maxSize = max(maxSize,len(window))
#                 window = window[window.index(l)+1:]+[l]
#             else:
#                 window.append(l)
        
#         return max(maxSize,len(window))

        charSet = set()
        l = 0
        ans = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l +=1
            charSet.add(s[r])
            ans = max(ans,r-l+1)
            
        return ans
        
                
        

        
        
        
        
        
        
        
        
        