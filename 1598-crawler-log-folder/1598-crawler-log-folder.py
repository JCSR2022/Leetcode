class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        #brute force asume only options are as explain in problem
        
        ans = 0
        
        for move in logs:
            #m = move.strip('/')
            m = move[:-1]
            #print(move,m)
            if m == "..":
                ans = max(0,ans-1)
            elif m == '.':
                pass
            else:
                ans += 1
            
        return ans
        