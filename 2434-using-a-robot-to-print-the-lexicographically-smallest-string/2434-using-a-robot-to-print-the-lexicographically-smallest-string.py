class Solution:
    def robotWithString(self, s: str) -> str:
        
        #hash_ch = Counter(s)
        #print(dict(hash_ch))

        hash_ch = [0]*26
        s_num = []
        for ch in s:
            ch_num = ord(ch)-ord('a')
            s_num.append(ch_num)
            hash_ch[ch_num] += 1

        #print(s_num)
        #print(hash_ch)

        pos_ch = 0
        while hash_ch[pos_ch] == 0:
            pos_ch += 1

        rest = []
        ans = []
        for ch_num in s_num:
            #print(ch_num,ans,rest)
            if ch_num == pos_ch:
                ans.append(ch_num)
                hash_ch[pos_ch] -= 1
                while hash_ch[pos_ch] == 0:
                    pos_ch += 1
                while rest and hash_ch[pos_ch] == rest[-1]:
                    ans.append(rest.pop())
                
            else:
                rest.append(ch_num)
        #print(ch_num,ans,rest)
        while rest:
            ans.append(rest.pop())
        #print(ch_num,ans,rest)

        return "".join([chr(ch_num+97)  for ch_num in ans  ])