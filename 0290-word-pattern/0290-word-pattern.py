class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s_list = s.split()
        
        if len(pattern) != len(s_list):
            return False
        
        map = {}
        for i,word in enumerate(s_list):
            if word not in map:
                if pattern[i] in map.values():
                    return False
                map[word] = pattern[i]
            else:
                if map[word] != pattern[i]:
                    return False
        return True