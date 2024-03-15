class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        # La forma mas facil seria multiplicar todo y despues 
        # dividir por nums[i] pero no es valida
        
        # Esto no es O(n)
        # def mult(lista):
        #     return reduce(lambda x, y: x * y, lista, 1)
        # return [mult(nums[:i] + nums[i+1:]) for i in range(len(nums))]
        
        # Sol O(n)  se recorre nums 3 veces
        size = len(nums)
        
        mult_1 = [nums[0]]
        for i in range(1,size-1):
            mult_1.append(mult_1[i-1]*nums[i])
        mult_1 = [1]+ mult_1
        
        mult_2 = [0]*(size-1)
        mult_2[-1] = nums[-1]
        for i in range(-2,-size,-1): 
            mult_2[i] = mult_2[i+1]*nums[i]
        mult_2.append(1)
        
        return [mult_1[i]*mult_2[i] for i in range(size)]
        
        