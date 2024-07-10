class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        #brute force asume only options are as explain in problem
        
        ans = 0
        
        for move in logs:
            #m = move.strip('/')
            #print(move,m)
            
            if move[:-1] == "..":
                ans = max(0,ans-1)
            elif move[:-1] == '.':
                pass
            else:
                ans += 1
            
        return ans
        