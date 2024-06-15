class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        # https://www.youtube.com/watch?v=1IUzNJ6TPEM
        # two heap pattern
        
        maxProfit = [] # only project can afford
        minCapital = [ (c,p)   for c,p  in zip(capital,profits)]
        
        heapq.heapify(minCapital)
        
        for i in range(k):
            
            while minCapital and minCapital[0][0] <= w:
                c,p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit,-1*p)
                
            if not maxProfit:
                break
            
            w += -1*heapq.heappop(maxProfit)
            
        return w
        
        
        
        
        
        
        
        #brute force : 
        # greedy find the most profit , on each level of capital needed choose the max profit project
        # @#%@#%@#%$#^#%^$#%#^Y%#
        
#         if min(capital) > w:
#             return w
        
        
#         hashCapProf = {}
#         for p,c in zip(profits,capital):
#             if p in hashCapProf:
#                 hashCapProf[p].append(c)
#             else:
#                 hashCapProf[p] = [c]
        
        
#         print(hashCapProf)
#         profits.sort(reverse=True)
#         print(profits)
        
#         while k > 0:
#             otbreak = False
#             for p in profits:
#                 for i,c in enumerate(hashCapProf[p]):
#                     print(p,c,w,k,hashCapProf)
#                     if c <= w:
#                         k -=1
#                         w += p
#                         del hashCapProf[p][i]
#                         otbreak = True
#                         break
#                 if otbreak: break
            
#         return w