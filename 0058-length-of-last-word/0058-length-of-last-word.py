class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cont = 0
        i = 0
        while  -1*(i-1)<=len(s) and s[i-1] == ' ':
            i -= 1
             
        while -1*(i-1)<=len(s) and  s[i-1] != ' ':
            cont +=1
            i -=1
        return cont
        