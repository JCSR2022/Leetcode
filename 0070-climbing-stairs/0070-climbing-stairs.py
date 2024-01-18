class Solution:
    def climbStairs(self, n: int) -> int:
        # Best explain: https://www.youtube.com/watch?v=Y0lT9Fck7qI
        
        one = 1
        two = 1
        
        for i in range(n-1):
            two,one = one, one+two
            
        return one
