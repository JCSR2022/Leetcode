class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        items.sort(key = itemgetter(0))
        max_beauty = [*accumulate(map(itemgetter(1), items), max, initial = 0)]
        return [max_beauty[bisect_right(items, q, key = itemgetter(0))] for q in queries]
        
        
#         #make a hash map
        
#         hash_price_beauty = {}
        
#         for p,b in items:
#             if p not in hash_price_beauty:
#                 hash_price_beauty[p] = b
#             else:
#                 hash_price_beauty[p] = max(b,hash_price_beauty[p])
                
#         print(hash_price_beauty)
        
#         price_beauty = [ (p,b) for p,b in hash_price_beauty.items()  ]
#         price_beauty.sort()
        
        
#         max_b = price_beauty[0][1]
#         for i in range(len(price_beauty)):
#             if max_b > price_beauty[i][1]:
#                 price_beauty[i]= (price_beauty[i][0],max_b)
#             else:
#                 max_b = price_beauty[i][1]
            
#         print(price_beauty)
        
        
#         # binary search:
#         l = price_beauty[0][0]
#         r = price_beauty[-1][0]
#         m = 
#         while l<r:
#             if m 
        
        
        
        
        
        
        
#         return [1,2]
            
                    
                    
                    
                
        