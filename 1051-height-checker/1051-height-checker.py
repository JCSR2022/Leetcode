class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # brute force oreder and compare
        
        orderHights = heights.copy()
        orderHights.sort()
        
        res = 0
        for ordH,hei in zip(orderHights,heights):
            if ordH != hei: res +=1
            
        return res