class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        
        #sol O(n), to be precise 2*n

        # dict_div_nums = {}
        # for n in nums:
        #     curr_div = n%value 
        #     if curr_div not in dict_div_nums:
        #         dict_div_nums[curr_div] = 1
        #     else:
        #         dict_div_nums[curr_div] += 1


        # for i in range(len(nums)):
        #     curr_div = i%value
        #     if curr_div in dict_div_nums and dict_div_nums[curr_div] != 0 :
        #         dict_div_nums[curr_div] -=1
        #     else:
        #         return i

        # return len(nums)

#-----------------------------------------------------------

#Vayase a la verga!! claro que es mas rapido pendejo ajajajaajaj


        # DP = [0] * value

        # for n in nums:
        #     DP[n % value] += 1
        
        # seed = 0
        # rounds = min(DP)
        
        # #This approach is faster than the one below.
        # for i in range(value):
        #     if DP[i] - rounds == 0:
        #         return (rounds * value) + i


#--------------------------------------------------------        

        #final  version
        
        dict_div_nums = {k:0 for k in range(value)}
        for n in nums:
                dict_div_nums[n%value] += 1


        rounds = min(dict_div_nums.values())

        for i in range(value):
            if dict_div_nums[i] - rounds == 0:
                return (rounds * value) + i
