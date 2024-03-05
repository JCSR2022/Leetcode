class Solution:
    def minimumLength(self, s: str) -> int:
        
#         if len(s) == 1:
#             return 1
        
#         L = 0
#         R = len(s)-1
        
#         while True:
#             print(L,R,s[L], s[R],s[L:R+1])
#             if s[L] != s[R]:
#                 return R-L+1
            
            
#             #Move left pointer:
#             while L + 1 < R and s[L+1] == s[L]: 
#                 L += 1
            
#             #Move right pointer:
#             while R - 1 > L and s[R-1] == s[R]:
#                 R -= 1
            
            
#             if L+1 == R:
#                 return 0
            
#             if L+2 == R:
#                 return 1
            
            

                
#             #Go to next letter
#             L += 1
#             R -= 1    
            
            left, right = 0, len(s) - 1
        
            while left < right and s[left] == s[right]:
                char = s[left]
                while left <= right and s[left] == char:
                    left += 1
                while right >= left and s[right] == char:
                    right -= 1

            return right - left + 1
        
                
            
        
        