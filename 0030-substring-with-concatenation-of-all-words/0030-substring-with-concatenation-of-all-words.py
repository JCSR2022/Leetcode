class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        
        
        if not s or not words:
            return []
        
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1
        
        substr_len = len(words) * len(words[0])
        word_len = len(words[0])
        result = []
        
        for i in range(len(s) - substr_len + 1):
            seen = defaultdict(int)
            for j in range(i, i + substr_len, word_len):
                word = s[j:j+word_len]
                if word in word_count:
                    seen[word] += 1
                    if seen[word] > word_count[word]:
                        break
                else:
                    break
            else:
                result.append(i)
        
        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #brute force: build arr ans size s 
        #for each letter review 
        # move a pointer through arr 
        # ceate the function to check letter of string mathc any concat on the elem in words
        
        #1 check if the letter is the first letter on a wrod in words
        #2 check if remaing letters exist on the word
        #3 mark as check , and go to the next word and the following letters
        #4 if all words then con +=1 and pointer is on the end of concat words
        #try to make al posible comb, of words? Not comb 5000!!!!!
        
        
        
        #using all info in problem and a hash map of words      
#         def checkWords(j,l,hash_w,words):
#             n = 0
#             while n < len(words):
#                 if not s[j+n*l:j+(n+1)*l] in hash_w:
#                     return False
#                 else:
#                     hash_w[s[j+n*l:j+(n+1)*l]] -=1
#                     if hash_w[s[j+n*l:j+(n+1)*l]] < 0:
#                         return False
#                 n += 1
#             return True
                
#         l = len(words[0])
        
#         hash_words = defaultdict(int)
#         for word in words:
#             hash_words[word] += 1
        
#         ans =[]
#         for i in range(len(s)-l*(len(words)-1)):
#             #print(i,s[i:i+l],checkWords(i,l,hash_words.copy(),words))
#             if checkWords(i,l,hash_words.copy(),words):
#                 ans.append(i)
    
#         return ans
        
        
        
        
        
        
        
        
        
        
        
        
# this is a general solution , dosent take the info that s is compose of only elements of words
# and does not use the info that all words have the same legth


#         def check_letter_word(i,checkWords):
#             word_exist = False
            
#             if i >= len(s):
#                 return word_exist,checkWords
            
#             for ind_word,w in enumerate(words):
#                 if w[0] == s[i]  and checkWords[ind_word] == 0 :
#                     if s[i:i+len(w)] == w:
#                         word_exist = True
#                         break
            
#             checkWords[ind_word] = 1
            
#             return word_exist , i+len(w)
                

#         ans = []    
#         for i in range(len(s)):
#             checkWords=[0]*len(words)
#             all_word_exist = False
#             j = i 
#             while sum(checkWords)<len(words):
#                 all_word_exist, j = check_letter_word(j,checkWords)
#                 if not all_word_exist:
#                     break
#             if all_word_exist:
#                 ans.append(i)
                
#         return ans
        
        
#---------------------------------------------------------------------------
        
        
#         def check_letter_word(i,checkWords):
#             word_exist = False
            
#             if i >= len(s):
#                 return word_exist,checkWords
            
#             for ind_word,w in enumerate(checkWords):
#                 if w[0] == s[i]:
#                     if s[i:i+len(w)] == w:
#                         word_exist = True
#                         break
#             checkWords.pop(ind_word)            
#             return word_exist , i+len(w)
                

#         ans = []    
#         for i in range(len(s)):
            
#             checkWords=words.copy()     
#             all_word_exist = False
#             j = i 
#             while checkWords and j <= len(s):
#                 all_word_exist, j = check_letter_word(j,checkWords)
#                 if not all_word_exist:
#                     break
#             if all_word_exist:
#                 ans.append(i)
                
#         return ans