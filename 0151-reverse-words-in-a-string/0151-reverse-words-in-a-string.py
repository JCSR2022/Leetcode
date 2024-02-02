class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([elem for elem in s.strip().split(" ") if elem != ''][::-1])
        