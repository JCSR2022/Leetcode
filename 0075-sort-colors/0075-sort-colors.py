class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.


        Dutch National Flag algorithm


        Use three pointers:

        low – the boundary for 0s.

        mid – the current index being inspected.

        high – the boundary for 2s.

        You iterate over the array using the mid pointer:

        If nums[mid] == 0: swap with nums[low], increment both low and mid.

        If nums[mid] == 1: it's already in the right place, just move mid forward.

        If nums[mid] == 2: swap with nums[high], decrement high. Do not increment mid yet, because the swapped element may be 0, 1, or 2.
        """
        


        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

        # L = 0
        # H = len(nums)-1
        # m = 1
        # #print(L,m,H,nums)
        # while m < H:
            
        #     if nums[m] == 0:
        #         nums[m],nums[L] = nums[L],nums[m]
        #         L +=1
        #         m +=1
        #     elif nums[m] == 1:
        #         m +=1
        #     else:
        #         nums[m],nums[H] = nums[H],nums[m]
        #         H -=1
        #     #print(L,m,H,nums)
        # if nums[L] == 2:
        #     nums[m],nums[L] = nums[L],nums[m]
        # #print(L,m,H,nums)
        # return nums










#---------------------------------------------------
        #just for fun 2*O(n)

        # hash_nums = Counter(nums)
        # nums[:] = [0]*hash_nums[0]+[1]*hash_nums[1]+[2]*hash_nums[2]




        #bubblesort n**2, iknow it is the less eficient!!
        # N = len(nums)
        # shift = True
        # while shift:
        #     shift = False
        #     for i in range(N-1):
        #         if nums[i]>nums[i+1]:
        #             nums[i], nums[i+1] = nums[i+1],nums[i]
        #             shift = True
        # return nums
    #----------------------------------------------------------------



        
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
        
        
            