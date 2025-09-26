class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        #lengths of triangle a,b,c have to be..
        # a+b > c , a+c> b and b+c> a ????
    #no se hoy no puedo, , necesito $7000.00 para seguir viviendo
        
        nums.sort()
        ans = 0
        for a in range(2, len(nums)):
            b, c = 0, a - 1
            while b < c:
                if nums[b] + nums[c] > nums[a]:
                    ans += c - b
                    c -= 1
                else:
                    b += 1
        return ans