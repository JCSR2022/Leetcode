class Solution:
    def frequencySort(self, s: str) -> str:
        map_letter = {}
        for letter in s:
            map_letter[letter] = map_letter.get(letter, 0) + 1
        
        sorted_list = sorted(map_letter.items(), key=lambda item: item[1], reverse=True)
        
        result = ""
        for elem,rept in sorted_list:
            result += elem*rept
        
        return result