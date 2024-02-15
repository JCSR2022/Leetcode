class Solution:
    def isValid(self, s: str) -> bool:
#         brackets = ['(' , ')' , '{' , '}', '[' , ']']
#         brackets_close = { ')': '(' , '}': '{',  ']':'[' }
        
#         if len(s) < 2:
#             return False
        
#         sequence = []
        
#         for elem in s:
#             if elem in brackets:
#                 if elem in brackets_close:
#                     if brackets_close[elem] in sequence and  brackets_close[elem] == sequence[-1]:
#                         sequence.pop()
#                     else:
#                         return False
#                 else:
#                     sequence.append(elem)
     
#         return len(sequence) == 0
          
        brackets_open =  ['(' , '{' , '[' ]
        brackets_close = [')' , '}' , ']' ]
        
        if len(s) < 2:
            return False
        
        sequence = []
        
        for elem in s:
            if elem in brackets_open:
                sequence.append(elem)
                
            if elem in brackets_close:
                if  ( (len(sequence) > 0)  and
                    (brackets_open[brackets_close.index(elem)] == sequence[-1])):
                    sequence.pop()
                else:
                    return False
     
        return len(sequence) == 0
                        
        