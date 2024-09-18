class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
#         #brute force tiem complexity : nLog(n) 
        

#         new_nums = [(int(str(n)[0]),len(str(n)), n) for n in nums]
#         print(new_nums)
        
#         new_nums.sort(key=lambda x:x[2], reverse =True )
#         new_nums.sort(key=lambda x:x[1] )
#         new_nums.sort(key=lambda x:x[0], reverse =True)
#         print(new_nums)
        
#         ans = ""
#         for elem in new_nums:
#             ans += str(elem[2])  
  
#         return ans


        for i,n in enumerate(nums):
            nums[i] = str(n)
            
        def compare(n1,n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
            
        nums.sort(key = cmp_to_key(compare) )
        
        if sum([int(n) for n in nums]) == 0:
            return "0"
        
        return "".join(nums)
