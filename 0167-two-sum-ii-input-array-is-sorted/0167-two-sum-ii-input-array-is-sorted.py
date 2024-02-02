class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # #brute force  O(n**2)  => n*(n-1)
        # for i,num in enumerate(numbers):
        #     for j in range(i+1,len(numbers)):
        #         if num+numbers[j] > target:
        #             break
        #         elif num+numbers[j] == target:
        #             return [i+1,j+1]
        
        i = 0
        j = len(numbers)-1
        while True:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1 
            elif numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            
        
        
        
        
        
        