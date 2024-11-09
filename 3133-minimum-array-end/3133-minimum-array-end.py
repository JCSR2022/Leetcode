class Solution:
    def minEnd(self, n: int, x: int) -> int:
        #create in order all posibles elements of arr
        
#         ans = [x]
#         num = x
#         while len(ans)<n:
#             num = (num+1) | x
#             ans.append(num)
        
#         #print(ans)
        
#         return ans[-1]
#-----------------------------------------
#         ans = x
#         for _ in range(n-1):
#             ans += 1
#             ans = ans | x
#         return ans
#-----------------------------------------       
    
    
        n_1, ans, j=n-1, 0, 0
        for i in range(56):
            if (x>>i)&1: 
                ans|=(1<<i)
            else:
                if (n_1>>j)&1: ans|=(1<<i)
                j+=1
        return ans