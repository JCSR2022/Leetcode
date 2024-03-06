class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window =[]
        maxSize = 0
        for l in s:
            if l in window:
                maxSize = max(maxSize,len(window))
                window = window[window.index(l)+1:]+[l]
            else:
                window.append(l)
        
        return max(maxSize,len(window))
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         window = []
#         maxSize = 0 
#         inic = 0
#         for letter in s:
#            # print(window,maxSize,letter)
#             if letter in window:
#                 maxSize = max(len(window),maxSize)
#                 inic += window.index(letter)
#               #  print("  inc:",inic)
#                 window = window[inic:]
            
#             else:
#                 window.append(letter)
                
#        # print(window,maxSize,letter)       
#         return max(len(window),maxSize)
        