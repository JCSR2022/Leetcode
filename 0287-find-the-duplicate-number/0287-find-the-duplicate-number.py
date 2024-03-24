from collections import Counter

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # this is the answer is There is only one repeated number in nums
        # n = len(nums)
        # return n -   (n*(n+1)//2 - sum(nums))
        
        """ this is the answer if  All the integers in nums appear only once except for precisely one integer which appears two or more times."""
        
        cont = Counter(nums)

        # Obtener una lista de tuplas de (valor, clave) ordenadas de mayor a menor
        most_common_items = cont.most_common()

        # Obtener la clave que contiene el valor máximo
        key_with_max_value = most_common_items[0][0]
        
        return key_with_max_value
        
        
    
        