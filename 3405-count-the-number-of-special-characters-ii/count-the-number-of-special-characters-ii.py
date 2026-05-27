class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        #aproach , working with flags?

        # #lower = set( n for n in range(97,123))
        # upper = set( n for n in range(65,90))

        # lowerSeen = set()
        # valids = set()

        # for ch in word:
        #     ascii_ch = ord(ch)
        #     if ascii_ch in upper:
        #         if ascii_ch-32 in lowerSeen:
        #             valids.add(ascii_ch)
        #     else:
        #         if ascii_ch+32 in valids:
        #             valids.remove(ascii_ch)  

        # return len(valids)     

#-------------------------------------------------------------
#maldita sea, piensa!!!!!!
#---------------------------------------------------
                
        # lower = 'abcdefghijklmnopqrstuvwxyz'
        # #upper = string.ascii_uppercase

        # invalid =set()
        # lowersee = set()
        # valid = set()
        # for ch in word:
        #     print(lowersee , valid, invalid)
        #     if ch.lower() in invalid:
        #         continue

        #     if ch in lower:
        #         if ch in valid:
        #             valid.remove(ch)
        #             invalid.add(ch)
        #         else:
        #             lowersee.add(ch)

        #     else:
        #         if ch.lower() in lowersee:
        #             valid.add(ch.lower())
        #         else:
        #             invalid.add(ch.lower() )
            
        # return len(valid)

#eres un maldito imbecil!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Output Limit Exceeded
#---------------------------------------------


        lower = { ch for ch in 'abcdefghijklmnopqrstuvwxyz'}

        last_lower = defaultdict(int)
        first_upper = defaultdict(int)

        for i,ch in enumerate(word):
            if ch in lower:
                last_lower[ch] = i

            else:
                if ch not in first_upper:
                    first_upper[ch] = i

        ans = 0
        for ch,indx in first_upper.items():
            if ch.lower() in last_lower and last_lower[ch.lower()] < indx:
                ans +=1
        return ans 


                



    








        