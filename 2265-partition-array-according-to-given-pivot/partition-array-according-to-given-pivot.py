class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        left  =[]
        right = []
        mid = []

        for n in nums:
            if n < pivot:
                left.append(n)
            elif n == pivot:
                mid.append(n)
            else:
                right.append(n)
        
        return left+mid+right


