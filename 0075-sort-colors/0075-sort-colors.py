class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        
        # counting sort 
        freq=[0]*3
        for x in nums: freq[x]+=1
        count=0
        for x in range(3):
            nums[count:count+freq[x]] = [x]*freq[x]
            count+= freq[x]
            
            
        
        # Dutch national flag problem (red, white, blue)
#         red, white, blue = 0, 1, 2
#         l, m, r = 0, 0, len(nums) - 1  # pointers to partition
        
#         while m <= r:
#             print(l,m,r,nums)
#             if nums[m] == red:
#                 nums[l], nums[m] = nums[m], nums[l]
#                 l += 1
#                 m += 1
#             elif nums[m] == white:
#                 m += 1
#             else:  # nums[m] == blue
#                 nums[m], nums[r] = nums[r], nums[m]
#                 r -= 1
        
        
        
        
        
        # bruteforce hasmap O(n):
        
#         hasMap = {}
#         for n in nums:
#             if n in hasMap:
#                 hasMap[n] += 1
#             else:
#                 hasMap[n] = 1
        
        
#         i = 0        
#         for color in [0,1,2]:
#             if color in hasMap:
#                 for j in range(i,i+hasMap[color]):
#                     nums[j] = color
#                 i += hasMap[color] 
        
        
            