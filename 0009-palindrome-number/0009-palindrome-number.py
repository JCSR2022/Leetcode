class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        str_x = str(x)
        size = len(str_x)
        mitad = size//2
        odd =  size%2
        if odd:
            return  str_x[:mitad] == str_x[-1:mitad:-1]
        else:
            return  str_x[:mitad] == str_x[-1:mitad-1:-1]

