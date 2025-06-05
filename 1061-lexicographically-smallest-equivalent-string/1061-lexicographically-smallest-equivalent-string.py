class my_find_change:
    def __init__(self):
        self.arr_letters = [i for i in range(26)]

    def find_letter(self,ch_num:int):
        while self.arr_letters[ch_num] != ch_num:
            ch_num = self.arr_letters[ch_num]
        return ch_num

    def change_letter(self,actual_ch:int,new_ch:int ):
        
        while self.arr_letters[new_ch] != new_ch:
            new_ch = self.arr_letters[new_ch]

        while self.arr_letters[actual_ch] != actual_ch:
            temp = self.arr_letters[actual_ch]
            self.arr_letters[actual_ch] = new_ch
            actual_ch = temp

        self.arr_letters[actual_ch] = new_ch

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        

#---------------------------------------------------------------

        base = my_find_change()

        s1_n = [ ord(ch)-ord('a') for ch in s1]
        s2_n = [ ord(ch)-ord('a') for ch in s2]
        baseStr_n = [ ord(ch)-ord('a') for ch in baseStr ]

        for ch1,ch2 in zip(s1_n,s2_n):
            n1 = base.find_letter(ch1)
            n2 = base.find_letter(ch2)

            if n1 < n2:
                base.change_letter(n2,n1)
            elif n1 > n2:
                base.change_letter(n1,n2)


        ans = [ chr( base.find_letter(ch) +ord('a') ) for ch in baseStr_n] 
        return "".join(ans)

#----------------------------------------------------------------

        # base = defaultdict(set)

        # for ch1,ch2 in zip(s1,s2):
        #     base[ch1].add(ch1)
        #     base[ch1].add(ch2)
        #     base[ch2].add(ch2)
        #     base[ch2].add(ch1)
    
        # base = {ch:sorted(list(re)) for ch,re in base.items() }

        # ans = [ base[ch][0] for ch in baseStr ]    

        # return "".join(ans)

#-------------------------------------------------------

        # base = {ch:ch for ch in string.ascii_lowercase}
        
        # for ch1,ch2 in zip(s1,s2):
        #     base[ch1] = min(base[ch1],ch2)
        #     base[ch2] = min(base[ch2],ch1)

        # for k,v in base.items():
        #     if k != v:
        #         print(k,v)
    
        # return "".join([base[ch] for ch in baseStr ])
