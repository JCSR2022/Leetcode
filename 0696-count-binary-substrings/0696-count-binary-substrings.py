class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        # count = {'0':0,'1':0}
        # prev = s[0]
        # on_review = False
        # for i in range(len(s)):
        #     if s[i] ==  

        # size = len(s)
        # if size == 1:
        #     return 0 

        # prev = s[0]
        # count_prev = 1
        # for ch in s[1:]:
        #     if ch == prev:
        #         count_prev += 1
        #     else:
                
                

        res = 0
        prev = 0
        strk = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]: strk += 1
            else:
                prev = strk
                strk = 1

            if strk <= prev: res += 1

        return res