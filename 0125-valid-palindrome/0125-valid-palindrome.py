class Solution:
    def isPalindrome(self, s: str) -> bool:
        list_string = [caracter.lower()  for caracter in s  if caracter.isalnum()]
        return list_string == list_string[::-1]
        