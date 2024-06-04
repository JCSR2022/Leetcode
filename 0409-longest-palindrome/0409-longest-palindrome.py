class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        #hashMap
        
        hashMap = {}
        
        for l in s:
            if l in hashMap:
                hashMap[l] +=1
            else:
                hashMap[l] = 1

        even_count = 0
        count = 0
        for k,x in hashMap.items():
            count += x 
            if x%2 != 0:
                even_count += 1
        return count - ( even_count - 1  if even_count > 0 else 0 )  
    
    
    
    
    