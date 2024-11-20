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
        R = 0
        while R < len(s):
            current_count[s[R]] -=1
            current_window_size += 1
            while current_count[s[R]] < k:
                current_count[s[L]] += 1
                current_window_size -= 1
                L += 1
        
            max_size =max(max_size,current_window_size)
            R += 1 
            
        return len(s)-max_size
    
    
    
    #----------------------------------------------------------------
        
        
#         if k == 0:
#             return 0
        
#         s_count = Counter(s)
#         if len(s_count.keys()) < 3: return -1
#         for v in s_count.values(): 
#             if v < k: return -1
            
            
#         current_count = s_count.copy()
#         print("#",current_count)
#         current_window_size = 0
#         max_size = 0
#         for i,letter in enumerate(s):
#             current_count[letter] -=1
#             print(i,current_count,max_size,current_window_size)
#             if current_count[letter] < k:
#                 current_count = s_count.copy()
#                 current_window_size = 0
#             else:
#                 current_window_size += 1
#                 max_size =max(max_size,current_window_size)
                
#         return len(s)-max_size