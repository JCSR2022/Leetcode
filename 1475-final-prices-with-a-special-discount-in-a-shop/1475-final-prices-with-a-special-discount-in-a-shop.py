class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        #brute force:
        
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



        stack = [prices[-1]]

        for i in range(len(prices) - 2, -1, -1):
            while stack and prices[i] < stack[-1]:
                stack.pop()

            tmp = prices[i]
            if stack:
                prices[i] -= stack[-1]

            stack.append(tmp)

        return prices
            