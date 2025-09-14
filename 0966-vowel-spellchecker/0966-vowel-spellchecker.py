class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        #Brute force

        def onlyConsonant(word):
            word = word.lower()
            new_word = ""
            for letter in word:
                if letter not in "AEIOUaeiou":
                    new_word += letter
                else:
                    new_word += "_"
            return new_word
        
        wordlist_lower = [ word.lower() for word in wordlist  ]
        wordlist_conso = [ onlyConsonant(word) for word in wordlist ]

        #print(wordlist_lower)
        #print(wordlist_conso)

        ans = []
        
        for q_word in queries:
            
            if q_word in wordlist:
                curr_ans = q_word

            elif q_word.lower() in wordlist_lower:
                curr_ans = wordlist[wordlist_lower.index(q_word.lower())]

            elif onlyConsonant(q_word) in wordlist_conso:
                curr_ans = wordlist[wordlist_conso.index(onlyConsonant(q_word))]
            
            else:
                curr_ans = ""
            ans.append(curr_ans)
        
        return ans



        