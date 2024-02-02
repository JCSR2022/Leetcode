class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = s.strip().split(" ")
        
        return " ".join([elem for elem in new_s if elem != ''][::-1])
        