class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        

        #aproach Brute force 
        # bitwise or is turning on all posible bits

        def find_bitwise(arr):
            bitwise = 0 
            for num in arr:
                bitwise |= num
            return bitwise

        maximum_possible_bitwise = find_bitwise(nums)
        ans = 0
        n = len(nums)
        for i in range(1, 2 ** n):
            bits = bin(i)[2:].zfill(n)  
            subset = [j for j, k in zip(nums,bits) if k == "1"]
            if find_bitwise(subset) == maximum_possible_bitwise:
                ans +=1

        return ans






        return 7

        













        #today i am not even trying , fuck the world, fuck life
        
        # Step 1: Find the maximum possible bitwise OR of the entire array
        # max_or = 0
        # for num in nums:
        #     max_or |= num
        
        # # Step 2: Helper function to recursively explore subsets and count those with max OR
        # def backtrack(index, current_or):
        #     if index == len(nums):
        #         return 1 if current_or == max_or else 0
        #     # Case 1: Include the current element in the subset
        #     include = backtrack(index + 1, current_or | nums[index])
        #     # Case 2: Exclude the current element from the subset
        #     exclude = backtrack(index + 1, current_or)
        #     return include + exclude
        
        # # Step 3: Start backtracking from index 0 and initial OR value 0
        # return backtrack(0, 0)
        