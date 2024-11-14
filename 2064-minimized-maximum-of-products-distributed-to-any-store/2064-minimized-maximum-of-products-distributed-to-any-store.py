class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # 1 calculate total of products and divide by n
        # 2 review quantities%expected if > adjust min
        
#         expected = int(round(sum(quantities)/n,0))
        
#         min_max = expected
        
#         for q in  quantities:
#             print(q,q//expected, q%expected)
#             if q//expected> 0 and q%expected>expected:
#                 min_max = max(min_max,q%expected+expected)  
#         return min_max
#NO        
#-----------------------------------------------------------------------

        def isditributed(prod_per_store):
            if prod_per_store == 0:
                return sum(quantities) <= n
            
            else:
                distribution = [math.ceil(p/prod_per_store) for p in  quantities]
            #print(prod_per_store, distribution,sum(distribution),  sum(distribution) <= n)
                return sum(distribution) <= n
        
        
        #binary search
        l = 0
        r = max(quantities)+1
        ans = r
        
        while l<=r and r>0:
            m =  r - (r-l)//2    #(l+r)//2
            print(l,r,m,ans)
            
            if isditributed(m):
                r = m-1
                ans = min(ans,m)
            else:
                l = m+1
                    
        return ans

        