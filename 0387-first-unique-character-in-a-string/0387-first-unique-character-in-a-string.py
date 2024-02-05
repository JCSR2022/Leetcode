class Solution:
    def firstUniqChar(self, s: str) -> int:
        map_letter = {}
        for letter in s:
            map_letter[letter] = 1 + map_letter.get(letter,0)
        
        for i,letter in enumerate(s):
            if map_letter[letter] == 1:
                return i
        return -1
        
        