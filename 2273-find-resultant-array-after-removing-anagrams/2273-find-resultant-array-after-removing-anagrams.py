class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        # ans = []
        # curr_hash = {}
        # for w in words:

        #     w_hash = {}
        #     for ch in w:
        #         if ch in w_hash:
        #             w_hash[ch] +=1
        #         else:
        #             w_hash[ch] = 1

        #     if curr_hash != w_hash:
        #         ans.append(w)
        #         curr_hash = w_hash
        
        # return ans

#---------------------------------------------------------       
#   do to 1 <= words[i].length <= 10 is posible sort is faster

        ans = []
        curr_w = []
        for w in words:
            new_w = sorted(list(w))
            if curr_w != new_w :
                ans.append(w)
                curr_w = new_w
        
        return ans