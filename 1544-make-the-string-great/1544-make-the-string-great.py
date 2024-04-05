class Solution:
    def makeGood(self, s: str) -> str:
        
        i = 0 
        while i < len(s)-1:
            #print(s,i,s[i+1],s[i].upper(),s[i+1] == s[i].upper(),s[:i] + s[i+2:]) 
            if (s[i+1] != s[i] and
                (s[i+1] == s[i].upper() or s[i+1].upper() == s[i])):
                s = s[:i] + s[i+2:]
                i = i-1
                if i < 0: i=0
                continue
            i += 1
                
        return s
        