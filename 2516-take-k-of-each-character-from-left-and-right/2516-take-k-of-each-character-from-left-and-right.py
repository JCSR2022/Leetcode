class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        
        #aproach: make a hash_map, find the max window that leave at least k of each letter out:
        
        
        if k == 0:
            return 0
        
        current_count = Counter(s)
        if len(current_count.keys()) < 3: return -1
        for v in current_count.values(): 
            if v < k: return -1
            
            
        current_window_size = 0
        max_size = 0
        L = 0 
        for R in range(len(s)):
            current_count[s[R]] -=1
            current_window_size += 1
            while current_count[s[R]] < k:
                current_count[s[L]] += 1
                current_window_size -= 1
                L += 1
            max_size =max(max_size,current_window_size)
     
        return len(s)-max_size
    

    
    
#         if k == 0:
#             return 0
        
#         current_count = Counter(s)
#         if len(current_count.keys()) < 3: return -1
#         for v in current_count.values(): 
#             if v < k: return -1
            
            
#         current_window_size = 0
#         max_size = 0
#         L = 0 
#         R = 0
#         while R < len(s):
#             current_count[s[R]] -=1
#             current_window_size += 1
#             while current_count[s[R]] < k:
#                 current_count[s[L]] += 1
#                 current_window_size -= 1
#                 L += 1
        
#             max_size =max(max_size,current_window_size)
#             R += 1 
            
#         return len(s)-max_size    
    #----------------------------------------------------------------
        

        
#         # Total counts
#         count = [0, 0, 0]
#         for c in s:
#             count[ord(c) - ord('a')] += 1

#         if min(count) < k:
#             return -1

#         # Sliding Window
#         res = float("inf")
#         l = 0
#         for r in range(len(s)):
#             count[ord(s[r]) - ord('a')] -= 1

#             while min(count) < k:
#                 count[ord(s[l]) - ord('a')] += 1
#                 l += 1
#             res = min(res, len(s) - (r - l + 1))
#         return res
        
