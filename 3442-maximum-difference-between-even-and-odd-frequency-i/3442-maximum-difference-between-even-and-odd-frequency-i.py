class Solution:
    def maxDifference(self, s: str) -> int:


        # s_hash = Counter(s)

        # odd_frec = 0
        # even_frec = float("inf")
        
        # for frec in s_hash.values():
        #     if frec%2 == 0:
        #         even_frec =min(even_frec,frec)
        #     else:
        #         odd_frec = max(odd_frec,frec)

        # return odd_frec - even_frec

#----------------------------------------------------
#faster?

        s_frec_arr = [0]*26
        for ch in s:
            s_frec_arr[ord(ch)-97] +=1

        print(s_frec_arr)

        odd_frec = 0
        even_frec = float("inf")
        for frec in s_frec_arr:
            if frec%2 == 0:
                even_frec =min(even_frec,frec)
            else:
                odd_frec = max(odd_frec,frec)
        print(odd_frec, even_frec)
        return odd_frec - even_frec








        