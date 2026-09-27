class Solution:
    def reverseParentheses(self, s: str) -> str:

        def reverse_word(i):
            
            return_word = ""
            while i < len(s) and s[i] != ')':
                if s[i] == '(':
                    curr_word,i = reverse_word(i+1)
                    return_word += curr_word
                else:
                    return_word += s[i]
                i += 1

            return return_word[::-1], i



        i = 0
        new_s = ""
        while i < len(s):
            curr_word = s[i] 
            if  curr_word == '(':
                curr_word,i = reverse_word(i+1)
            new_s += curr_word
            i +=1
        
        return new_s


        