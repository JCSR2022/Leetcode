class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_vol = 0 
        i = 0
        j = len(height)-1

        while i < j:
            act_vol =  min(height[i],height[j])*(j-i)
            if act_vol > max_vol:
                max_vol = act_vol
            if height[i] <= height[j]:
                i = i + 1
            else:
                j = j - 1
                    
        return  max_vol