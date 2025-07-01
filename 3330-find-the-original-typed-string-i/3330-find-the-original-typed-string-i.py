class Solution:
    def possibleStringCount(self, word: str) -> int:

        #aproach , O(n), make hash_word
        # hash_word = Counter(word)

        # ans = 0
        # for ch,cnt in hash_word.items():
        #     if cnt > 1:
        #         ans += cnt-1
        # return ans + 1 

#noooooooo word = "ere" expected =1
#----------------------------------------------------------
        
        #same idea just will work

        # ans = 0
        # prev_ch = ''
        # for ch in word:
        #     if ch == prev_ch:
        #         ans += 1
        #     else:
        #         prev_ch = ch

        # return ans +1

#---------------------------------------------------
        #faster and cleaner

        ans = 1
        for i in range(1,len(word)):
            if word[i-1] == word[i]:
                ans += 1
        return ans








        #she is aware that she may still have done this at most once.
        #"abbcccc"
        #"abcccc"
        #"abbccc"
        #"abbccc"
        #"abbccc"

        #she may still have done this at least once.
        #"abbcccc"
        #"abbccc"
        #"abbcc"
        #"abbc"
        #"abcccc"
        #"abccc"
        #"abcc"
        #"abc"