class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        
        #brute force:

        # MOD = 10**9+7


        # shift = {}
        # letters = list(string.ascii_lowercase)
        # for i in range(0,len(letters)-1):
        #     shift[letters[i]] =[letters[i+1]]
        # shift['z'] = ['a','b']


        # hash_s = Counter(s)
        # #print(dict(hash_s))
        # for _ in range(t):
        #     new_hash = defaultdict(int)
        #     for letter,cnt in  hash_s.items():
        #         for ch in shift[letter]:
        #             new_hash[ch] = (new_hash[ch]+ cnt)%MOD
        #             #print(letter,dict(new_hash))

        #     hash_s = new_hash 
        #     #print(dict(hash_s))
        
        # return sum(hash_s.values())%MOD

#Time Limit Exceeded
#------------------------------------------------
    #{a} after 26 shift become {z}
    #{z} =>{a,b} after 25 shifts {y,z} 



        MOD = 10**9+7

        hash_s_num = [0]*26
        for i in [ord(ch) - ord('a') for ch in s ]:
            hash_s_num[i] += 1

        for _ in range(t):
            new_hash_s = [0]*26
            for i in  range(25):
                new_hash_s[i+1] = hash_s_num[i]

            new_hash_s[0]  = hash_s_num[25]
            new_hash_s[1] += hash_s_num[25]
              
            hash_s_num = new_hash_s 
                
        return sum(hash_s_num)%MOD