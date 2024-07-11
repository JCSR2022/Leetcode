class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        # two steps pointer find i for all ( ,until find ) 
        # save the letters on strign and reverse according to pointers
        
        pointer =[]
        letters = []
        
        i = 0 
        for l in s:

            if l == "(":
                pointer.append(i)
            elif l == ")":
                left = pointer.pop()
                arr = letters[left:i]
                letters[left:i] = arr[::-1]
            else:
                letters +=[l]
                i +=1
        
        return "".join(letters)
            
        