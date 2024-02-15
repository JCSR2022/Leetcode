class Solution:
    def isValid(self, s: str) -> bool:
        brackets = ['(' , ')' , '{' , '}', '[' , ']']
        brackets_close = { ')': '(' , '}': '{',  ']':'[' }
        
        if len(s) < 2:
            return False
        
        sequence = []
        
        for elem in s:
            if elem in brackets:
                if elem in brackets_close:
                    if brackets_close[elem] in sequence and  brackets_close[elem] == sequence[-1]:
                        sequence.pop()
                    else:
                        return False
                else:
                    sequence.append(elem)
        ans = len(sequence) == 0
        return ans
                        
                        
        