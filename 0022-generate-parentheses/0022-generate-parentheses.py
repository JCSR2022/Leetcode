class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # aproach: dfs
        # count the '(' inserted and the ')' 
        #   push and pop acording to count
        #   '('      open =1 close =0
        #   '(('     open =2 close =0
        #   '((('    open =3 close =0
        #   '((()'   open =3 close = 1
        #   validis  open = close , open and close < n
        # constructtion of tree makes always ..(....)...
        
        ans = []
        def dfs(pare,op,cl):
            #print(pare,op,cl,ans)
            
            if op > n or cl > n :
                return
            
            if op == cl and op == n :
                ans.append(pare)
            
            
            if cl<= op: dfs(pare+"(",op+1,cl)
            dfs(pare+")",op,cl+1)        
                
        dfs("",0,0)
   
        return ans
            
            