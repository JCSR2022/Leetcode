class Solution:
    def firstUniqChar(self, s: str) -> int:
        map_letter = {}
        for letter in s:
            map_letter[letter] = 1 + map_letter.get(letter,0)
        
        for i,letter in enumerate(s):
            if map_letter[letter] == 1:
                return i
        return -1
        
#         map_letter = {}
#         for i,letter in enumerate(s):
#             if letter in map_letter:
#                 map_letter[letter] = float("inf")
#             else:
#                 map_letter[letter] = i
                
#         min_index = min(map_letter.values(), default=-1)
#         return min_index if min_index != float("inf") else -1
        
        
        
        