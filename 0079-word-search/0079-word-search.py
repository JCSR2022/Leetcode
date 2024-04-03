class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        """ No pude hacerlo funcionar::: @%#@$@$@!!!!!!!        
                cell_used = [ [False for _ in board[0]] for _ in board ]
                ans = [False]
                def dfs(i,j,k=0,ans=ans):
                    print(i,j,board[i][j],word[k],ans)
                    if  (i >= 0 and 
                        i <= len(board)-1 and 
                        j >= 0 and 
                        j <= len(board[0])-1 and
                        k <  len(word)-1 and 
                        not cell_used[i][j]):

                        if  board[i][j] == word[k]:
                            cell_used[i][j] = True
                            if k == len(word) - 1:
                                ans = [True]

                            dfs(i+1,j,k+1)
                            dfs(i+-1,j,k+1)
                            dfs(i,j+1,k+1)
                            dfs(i,j-1,k+1)

                            cell_used[i][j] = False

                for i in range(len(board)):
                    for j in range(len(board[0])):
                         dfs(i,j)

                return ans[0]
        """ 
        rows , cols = len(board), len(board[0])
        
        path = set()
        
        def dfs(r,c,i=0):
            if i == len(word):
                return True
            
            if (r < 0 or c < 0 or 
                r>=rows or c >= cols or
                word[i] != board[r][c] or (r,c) in path):
                return False
            
            path.add((r,c))
            res = ( dfs(r+1,c,i+1) or
                    dfs(r-1,c,i+1) or
                    dfs(r,c+1,i+1) or
                    dfs(r,c-1,i+1) )
            
            path.remove((r,c))
            return res
     
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c): return True
        
        return False
            
                
    
    