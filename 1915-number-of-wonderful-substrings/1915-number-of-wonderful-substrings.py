class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        
        # brute force
         
#         def checkWonderfull(s):
#             count_letters = {}
            
#             for l in s:
#                 if l in count_letters:
#                     count_letters[l] += 1
#                 else:
#                     count_letters[l] = 1
            
#             count_odd = 0
#             for l_val in count_letters.values():
#                 if l_val % 2 != 0 :
#                     count_odd += 1
                    
#             #print('s',count_letters,count_odd)
            
#             if count_odd > 1:
#                 return False
#             return True
                
        
#         count_wonderful = 0
#         for i in range(len(word)):
#             for j in range(i + 1, len(word) + 1):
#                 if checkWonderfull(word[i:j]):
#                     count_wonderful +=1
#                 #print(word[i:j],count_wonderful)
        
#         return count_wonderful
# #
#  -------------------------------
    
        # using dp and a Mask
        
        mask = 0
        
        cnt = defaultdict(int)
        cnt[0] = 1
        
        ans = 0
        
        for c in word:
            index = ord(c) - ord('a')
            mask ^= (1<<index)
            ans += cnt[mask] # all letter appears an even number of times
            
            # one letter appears an odd number of times
            
            for i in range(10):
                preMask = mask ^ (1<<i)
                ans += cnt[preMask]
                
            cnt[mask] += 1
        
        
        
        return ans
        
        
        
        
        
        
        
        