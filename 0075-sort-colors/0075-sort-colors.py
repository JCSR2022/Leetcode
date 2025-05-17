class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        


        #bubblesort n**2

        N = len(nums)

        shift = True
        while shift:
            shift = False
            for i in range(N-1):
                if nums[i]>nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1],nums[i]
                    shift = True
        return nums
                
















        
        
        # # counting sort (it is the same as HasMap sol)
        # freq=[0]*3
        # for x in nums: freq[x]+=1
        # count=0
        # for x in range(3):
        #     nums[count:count+freq[x]] = [x]*freq[x]
        #     count+= freq[x]
            
            
        
        # # Dutch national flag problem (red, white, blue)
        # red, white, blue = 0, 1, 2
        # l_red, m_white, r_blue = 0, 0, len(nums) - 1  # pointers to partition
        
        # while  m_white <=  r_blue:
        #     print(l_red, m_white, r_blue,nums)
        #     if nums[m_white] == red:
        #         nums[l_red], nums[m_white] = nums[m_white], nums[l_red]
        #         l_red += 1
        #         m_white += 1
        #     elif nums[m_white] == white:
        #         m_white += 1
        #     else:  # nums[m] == blue
        #         nums[m_white], nums[ r_blue] = nums[r_blue], nums[m_white]
        #         r -= 1
        
        
        
        
        
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
        
        
            