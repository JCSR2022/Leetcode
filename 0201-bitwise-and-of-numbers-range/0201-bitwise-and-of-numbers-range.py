class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        # #Brute force 
        # if left == right:
        #     return left
        # ans = left
        # for x in range(left+1, right+1):
        #     #print((x,bin(x)),(ans,bin(ans)),(x&ans,bin(x&ans)))
        #     ans = x&ans  
        #     if ans == 0:
        #         return ans
        # return ans
        
        i = 0 
        while left != right:
            left = left >> 1
            right = right >> 1
            i += 1
        
        return left << i  
        