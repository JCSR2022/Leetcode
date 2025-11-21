class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:




        # #brute force 3 pointers n**3 again!!!
        # size = len(s)
        # ans = set()
        # for i in range(size-2):
        #     for j in range(i+1,size):
        #         for k in range(j+1,size):
        #             if s[i] == s[k]:
        #                 ans.add(s[i]+s[j]+s[k])
        #             print((i,j,k),s[i],s[j],s[k],s[i] == s[k],ans)
        # return len(ans) 
#------------------------------------------------------------------------------------   

#no tengo idea de como lo resolvi, y no lo puedo resolver otra vez @#%$#^$^$

        #brute force: 3 pointers n**3

        # palind = set()
        # for i in range(len(s)-2):
        #     for j in range(i+1,len(s) -1):
        #         for k in range(j+1,len(s)):
        #             if s[i] == s[k] and s[i]+s[j]+s[k] not in palind :
        #                 palind.add(s[i]+s[j]+s[k])
        # return len(palind)

#work but Time Limit Exceeded
#------------------------------------------------------------
        #O(n) sol

        palind = set() 
        left = set()
        right = Counter(s)

        for mid_ch in s:
            #print(mid_ch,left,dict(right),palind)
            #print()
            right[mid_ch] -= 1
            for ch in left:
                if right[ch] > 0 :
                    palind.add(ch+mid_ch+ch)
            left.add(mid_ch)
        #print(mid_ch,left,dict(right),palind)
        return len(palind)


#---------------------------------------------------------------------------
        #high on drogs sol
        
        # R = [0] * 26
        # for u in s:
        #     R[ord(u) - ord('a')] += 1
        
        # L = [0] * 26
        # S = set()
        
        # for i in range(len(s)):
        #     t = ord(s[i]) - ord('a')
        #     R[t] -= 1
        #     for j in range(26):
        #         if L[j] > 0 and R[j] > 0:
        #             S.add(26 * t + j)
        #     L[t] += 1
        
        # return len(S)

        
