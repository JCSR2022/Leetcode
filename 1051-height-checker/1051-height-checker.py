class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        # brute force oreder and compare
        expected = heights.copy()
        expected.sort()
        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]: res +=1
            
        return res

  