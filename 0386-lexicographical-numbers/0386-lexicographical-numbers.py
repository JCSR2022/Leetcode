class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        
        #n_str = list(str(n))
        #print(n_str)
        
        ans = [ str(x) for x in range(1,n+1)]
        ans.sort()
        
        return [ int(x) for x in ans]