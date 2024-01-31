class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def map_string(string):
            map_s = {}
            for letter in string:
                if letter in map_s:
                    map_s[letter] +=1
                else:
                    map_s[letter] = 1
            return map_s
        
        map_s = map_string(s)
        map_t = map_string(t)
        
        return map_t == map_s
        