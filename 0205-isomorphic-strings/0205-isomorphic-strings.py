class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
       # map_chars = {}
       # for i, char_s in enumerate(s):
       #     if char_s not in map_chars:
       #         if t[i] not in map_chars.values():
       #             map_chars[char_s] = t[i]
       #         else:
       #             return False
       #     else:
       #         if map_chars[char_s] != t[i]:
       #             return False
       # return True
    
    
        mapping_s_t = {}
        mapping_t_s = {}

        if len(s) != len(t):
            return False

        for char_s, char_t in zip(s, t):
            if char_s in mapping_s_t:
                if mapping_s_t[char_s] != char_t:
                    return False
            else:
                mapping_s_t[char_s] = char_t

            if char_t in mapping_t_s:
                if mapping_t_s[char_t] != char_s:
                    return False
            else:
                mapping_t_s[char_t] = char_s

        return True
    