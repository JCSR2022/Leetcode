class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # brute force as you

        # size = len(s)
        # window = {'a':0,'b':0,'c':0}
        # i = 0
        # j = 0
        # ans = 0
        # while j < size:
        #     window[s[j]] += 1
        #     j +=1
        #     allpresent = True
        #     while allpresent:
        #         for k,v in window.items():
        #             if v == 0: 
        #                 allpresent = False
        #                 break
        #         if allpresent:
        #             ans += size-j+1
        #             window[s[i]] -=1
        #             i +=1
                
        # return ans

#no mames!!!!! que belleza
#-------------------------------------------------------------------------
        last = {'a': -1, 'b': -1, 'c': -1}
        result = 0
        
        for i, ch in enumerate(s):
            last[ch] = i
            result += 1 + min(last['a'], last['b'], last['c'])
        
        return result