class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        
        #sol O(n), to be precise 2*n


        arr = [n%value for n in nums]
        dict_div_nums = Counter(arr)

        for i in range(len(nums)):
            if i%value in dict_div_nums:
                dict_div_nums[i%value] -=1
                if  dict_div_nums[i%value] == 0:
                    del dict_div_nums[i%value]
            else:
                return i

        return len(nums)

