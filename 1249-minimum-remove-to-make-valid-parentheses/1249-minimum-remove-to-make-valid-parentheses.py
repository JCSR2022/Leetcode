class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # aproach 
        # make a stack with the left parentesis postions 
        # for every time a right parentisis apears remove from the stack a left parentisis
        #       if not left parentisis in stack then remove from s that rigth parentesis 
        # at the end repove from s all left parentesis 
        
        
        left = []
        list_to_remove = []
        for i,c in enumerate(s):
            ## print(list_to_remove,left)
            if c == '(':
                left.append(i)
            if c == ')':
                if len(left) == 0:
                    list_to_remove.append(i)
                else:
                    left.pop()
                    
        list_to_remove += left
        # print(list_to_remove)
        for i,elem in enumerate(list_to_remove):
            # print(s)
            s = s[:elem-i]+ s[elem+1-i:]
                    
        return s
        