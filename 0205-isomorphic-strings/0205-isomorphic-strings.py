class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        map_chars = {}
        for i, char_s in enumerate(s):
            if char_s not in map_chars:
                if t[i] not in map_chars.values():
                    map_chars[char_s] = t[i]
                else:
                    return False
            else:
                if map_chars[char_s] != t[i]:
                    return False
        return True