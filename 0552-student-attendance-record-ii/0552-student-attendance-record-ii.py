class Solution:
    def checkRecord(self, n: int) -> int:

        cache = {}
    
        def count(n):
            # matrix will keep record of status of A and L
            # matrix (A,L), A can take only 0 and 1 val, L can take 0,1,2
            # n = 1 (Base case)
            #       L      0                       1                             2
            #       --------------------------------------------------------------------
            #     A  0  |   1(1P 0L 0A)    1(0P 1L 0A  )                  0(cant have 2L n =1)   
            #        1  |   1(0P  0L 1A)   0(cant have 0P 1L 1A n =1  )   0(cant have 2L 1A n =1)
            #
            #n = 2 from n1 adding a P
            #       L      0                                                   1          2
            #       --------------------------------------------------------------------
            #     A  0  |   2(PP and LP ->M(-1)[0,0]+M(-1)[0,1]+M(-1)[0,2])    0         0   
            #        1  |   1(AP ->M(-1)[1,0]+M(-1)[1,1]+M(-1)[1,2])           0         0
            #
            #n = 2 from n1 adding a L 
            #       L      0                       1                       2
            #       --------------------------------------------------------------------
            #     A  0  |   0          1( PL ->M(-1)[0,0]  )           1( LL ->M(-1)[0,1])   
            #        1  |   0          1 ( AL ->M(-1)[1,0] )           0 ( -> M(-1)[1,1])  
            #
            #n = 2 from n1 adding a A  
            #       L      0                                                      1    2
            #       --------------------------------------------------------------------
            #     A  0  | 0( not pos  )                                         0    0   
            #        1  | 2(PA,LA, LLA* ->M(-1)[0,0]+M(-1)[0,1]+M(-1)[0,2])     0    0
            #
            #  n = 2
            #       L      0                       1                             2
            #       --------------------------------------------------------------------
            #     A  0  |   2                    1                             1
            #        1  |   3                    1                             0
            #  sum(MAtrix) = 8 
            
            
            if n in cache:
                return cache[n]
            
            
            if n == 1:
                         return {
                    (0,0):1 , (0,1):1, (0,2): 0,
                    (1,0):1 , (1,1):0, (1,2): 0
                    }
        
    
            temp = count(n-1)
            res = defaultdict(int)
            
            
            # chose P (adding a P)
            res[(0,0)] = (temp[(0,0)] + temp[(0,1)] + temp[(0,2)]) % MOD
            res[(1,0)] = (temp[(1,0)] + temp[(1,1)] + temp[(1,2)]) % MOD
            
            # chose L (adding a L)
            res[(0,1)] = temp[(0,0)] % MOD
            res[(0,2)] = temp[(0,1)] % MOD
            res[(1,1)] = temp[(1,0)] % MOD
            res[(1,2)] = temp[(1,1)] % MOD
            
            #Chose A  (adding a A)
            res[(1,0)] += (temp[(0,0)] + temp[(0,1)] + temp[(0,2)])% MOD
            
            cache[n] = res
            
            return res 
        
    
        MOD = 10**9 + 7 
        ans = sum(count(n).values())
        
        return ans % MOD
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # brutal stupid way
#         posibles = [''.join(p) for p in itertools.product('ALP', repeat=n)]
        
#         print(posibles,len(posibles))
        
#         ans_n = 0
#         #ans = []
#         for op in posibles:
#             if 'LLL' not in op  and op.count('A') < 2:
#                 #ans.append(op)
#                 ans_n +=1
#         #print(ans,len(ans))
        
#         return ans_n

# # all posible com is n**3 ('ALP') 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        