class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        
        #same aproach dp? will not work t> 10**8

        MOD = 10**9+7

        s_num = [ord(ch)-ord('a') for ch in s ]

        s_hash = [0]*26
        for i in s_num:
            s_hash[i] += 1

        #print(s_hash)
        for trans in range(t):
            new_s_hash = [0]*26
            for ch,ch_cnt in enumerate(s_hash):
                if ch_cnt > 0 :
                    for n_ch in range(ch+1,ch+1+nums[ch]):
                        new_s_hash[n_ch%26] += ch_cnt
            s_hash = new_s_hash           
            #print(s_hash)

        return sum(s_hash)%MOD







             

