class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # #brute force  O(n**2)  => n*(n-1)
        # for i,num in enumerate(numbers):
        #     for j in range(i+1,len(numbers)):
        #         if num+numbers[j] > target:
        #             break
        #         elif num+numbers[j] == target:
        #             return [i+1,j+1]
        
        left = 0
        right = len(numbers)-1 
        
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1 
            else:
                return [left+1,right+1]
        return 0
        
        
        
        
        
        