class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        # use two pointers to move trhu nums1 and mums2 
        # if nums1[p1] == nums[p2] return nums1[p1]
        # move the pointer with min value on numsX   
        #     check if nums1[p1] >= nums2[p2]:
        #            p2 +=1 
        # repeat all this while p1< len(nums1) and p2 < <len(nums2)
        
        p1 = 0
        p2 = 0 
        
        ans = -1
        
        while (p1 < len(nums1)) and (p2 < len(nums2)):
            
            if nums1[p1] == nums2[p2]:
                return nums1[p1]
            elif nums1[p1] >= nums2[p2]:
                p2 += 1
            else:
                p1 +=1 
            
        return ans
            
        
        