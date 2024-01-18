class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # map_chars = {}
        # for i, char_s in enumerate(s):
        #    if char_s not in map_chars:
        #        if t[i] not in map_chars.values():
        #            map_chars[char_s] = t[i]
        #        else:
        #            return False
        #    else:
        #        if map_chars[char_s] != t[i]:
        #            return False
        # return True
    
        map_chars = {}
        for char_s, char_t in zip(s, t):
            if char_s not in map_chars:
                if char_t not in map_chars.values():
                    map_chars[char_s] = char_t
                else:
                    return False
            else:
                if map_chars[char_s] != char_t:
                    return False
        return True    
            
    