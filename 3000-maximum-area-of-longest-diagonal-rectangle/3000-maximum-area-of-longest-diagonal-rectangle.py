class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:

        #brute as you

        ans = [0,0] #long_dia**2,max_area
        for length,width in dimensions:
            curr_diag2 = length**2 + width**2 
            if curr_diag2 == ans[0]:
                ans[1] = max(length*width, ans[1])    
            elif curr_diag2 > ans[0]:
                ans[0],ans[1] = curr_diag2, length*width

        return ans[1]
            
        
        