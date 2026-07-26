class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        # nums.sort()
        # return max( nums[0]*nums[1]*nums[-1],nums[-3]*nums[-2]*nums[-1])

#-----------------------------------------------------------------------------
#imbecil solo ubica los 2 mas pequenos y los 3 mas grandes


        min1 = 1002
        min2 = 1001

        max1 = -1003
        max2 = -1002
        max3 = -1001

        for n in nums:
            #check min
            if n <= min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n


            #check max
            if n >= max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n >= max2:
                max3 = max2
                max2 = n
            elif n > max3:
                max3 = n
        
            #print(n, min1,min2,max1,max2,max3 )
        
        return max( min1*min2*max1 , max1*max2*max3 )