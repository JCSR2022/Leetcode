class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        indx1 = nums.index(max(nums))
        indx2 = nums.index(min(nums))
        size = len(nums)

        left = min(indx1,indx2)
        right = max(indx1,indx2)
        #print(left,right)

        opc1 = (left+1) + (size - right)
        #print(opc1)

        opc2 = right+1   
        #print(opc2)

        opc3 = size - left 
        #print(opc3)

        return min(opc1,opc2,opc3)