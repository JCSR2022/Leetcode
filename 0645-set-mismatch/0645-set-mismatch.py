class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

       # numeros = [n for n in range(1,len(nums)+1)]
       # faltante = 0
       # repetido = 0
       # for num in numeros:
       #     if num not in nums:
       #         faltante = num
       #     else:
       #         nums.pop(nums.index(num))
       # repetido = nums[0]
       # return [repetido,faltante]
        
        numeros = { n: 0 for n in range(1,len(nums)+1)} 

        for num in nums:
            numeros[num] +=1
            if numeros[num] == 2:
                repetido = num

        for key, value in numeros.items():
            if value == 0:
                faltante = key
                break
        return [repetido,faltante]
                
        
        