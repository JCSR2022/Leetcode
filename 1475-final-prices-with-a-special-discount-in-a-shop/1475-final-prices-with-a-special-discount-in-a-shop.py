class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        #brute force: O(n**2)
        
#         ans = []
#         for i,price_i in enumerate(prices):
#             j = i+1
#             while j < len(prices):
#                 if prices[j] <= price_i:
#                     ans.append(price_i-prices[j])
#                     break
#                 else:
#                     j +=1
#             if j == len(prices):
#                 ans.append(price_i)
                
#         return ans

#---------------------------------------------------


#         price = [8,7,4,2,8,1,7,7,10,1]
#         arr = [ (val,i) for i,val in enumerate(prices) ]
#         #arr.sort(key=lambda x: (x[1], x[0]))
#         #ordena por valor de forma decreciente
#         arr.sort(key=lambda x: x[0])
#         #ordena por indice de forma creciente
#         arr.sort(key=lambda x: x[1], reverse=True) 
#         print(arr)
        
#         return prices



#--------------------------------------------------



#         result = prices.copy()
#         stack = []
#         for i, p in enumerate(prices):
#             while stack and p <= stack[-1][0]:
#                 _, j = stack.pop()
#                 result[j] -= p
            
#             stack.append((p, i))

#         return result


#---------------------------------------------


        discount = [0]*len(prices)
        stack = []
        
        for i in range(len(prices)-1,-1,-1):
            while stack and stack[-1] > prices[i]:
                stack.pop()
                
            if stack:
                discount[i] = stack[-1]
                
            stack.append(prices[i])
            
        
        return [ p-d for p,d in zip(prices,discount) ]
            
        
                





















