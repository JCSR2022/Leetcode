class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
#         # brute force oreder and compare
#         expected = heights.copy()
#         expected.sort()
#         res = 0
#         for i in range(len(heights)):
#             if heights[i] != expected[i]: res +=1
            
#         return res



# 1 <= heights.length <= 100
# 1 <= heights[i] <= 100
        # using an sort method fast for small arr
    
        count = [0 for n in range(101)]

        for h in heights:
            count[h] += 1
        
        expected = []
        for i,n in enumerate(count):
            if n > 0:
                expected += [i]*n
                
        #print(expected)
        
        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]: res +=1
            
        return res
        
            
