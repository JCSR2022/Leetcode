class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        
        #sol O(n), to be precise 2*n

        dict_div_nums = {}
        for n in nums:
            curr_div = n%value 
            if curr_div not in dict_div_nums:
                dict_div_nums[curr_div] = 1
            else:
                dict_div_nums[curr_div] += 1


        for i in range(len(nums)):
            curr_div = i%value
            if curr_div in dict_div_nums and dict_div_nums[curr_div] != 0 :
                dict_div_nums[curr_div] -=1
            else:
                return i

        return len(nums)

