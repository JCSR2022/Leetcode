class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        def can_form_word(w,letter_cnt):
            word_cnt = Counter(w)
            for c in word_cnt:
                if word_cnt[c] > letter_cnt[c]:
                    return False
            return True
        
        letter_score = {}
        for i,letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
            letter_score[letter] = score[i]
        def get_score(w):
            return sum([letter_score[x] for x in w])
        
        
        letter_cnt = Counter(letters)
        def backtrack(i):

            if i == len(words):
                return 0
            
            res = backtrack(i+1) # skip word
            
            if can_form_word(words[i],letter_cnt):
                
                for c in words[i]:
                    letter_cnt[c] -= 1
                
                res = max(res,get_score(words[i])+ backtrack(i+1)  )
                
                for c in words[i]:
                    letter_cnt[c] += 1
                    
            return res
        
        return backtrack(0)
                
                
                
                
                
                
        
        
        
        
        
#------------------------------------------------------           
#         counter = Counter(letters)
#         n = len(words)
        
#         def backTrack(start,letter_counter):
#             if start == n:
#                 return 0
            
#             ans = 0
            
#             for i in range(start,n):
#                 temp_counter = copy.deepcopy(letter_counter)
#                 word = words[i]
#                 word_score = 0
#                 isValid = True
                
#                 for c in word:
#                     if c in temp_counter and temp_counter[c] > 0:
#                         temp_counter[c] -= 1
#                         word_score += score[ord(c)-ord('a')]
#                     else:
#                         isValid = False
#                         break
                   
#                 if isValid:
#                     ans = max(ans,backTrack(i+1,temp_counter) + word_score)
                    
#             return ans 
        
        
#         return backTrack(0,counter)
        
#------------------------------------------------------    
        
#         Letters_hash = {}
#         for letter in letters:
#             if letter in Letters_hash:
#                 Letters_hash[letter] += 1
#             else:
#                 Letters_hash[letter] = 1
        
        
#         letter_score = {}
#         for i,letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
#             letter_score[letter] = score[i]
        
        
#         print(Letters_hash)
#         print(letter_score)
        
        
#         return 0 