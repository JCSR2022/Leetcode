class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        #for i,num in enumerate(nums):
        #    if num != i+1:
        #        return [num,i+1]
        numeros = [n for n in range(1,len(nums)+1)]
        faltante = 0
        repetido = 0
        for num in numeros:
            if num not in nums:
                faltante = num
            else:
                nums.pop(nums.index(num))
        repetido = nums[0]
        return [repetido,faltante]
                
        
        