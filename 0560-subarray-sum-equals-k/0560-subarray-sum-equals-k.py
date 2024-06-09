class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        #https://www.youtube.com/watch?v=fFVZt-6sgyo
        
        res = 0
        curSum = 0
        prefixSums = {0:1}
        
        for n in nums:
            curSum += n
            diff = curSum - k
            
            res += prefixSums.get(diff,0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum,0)
            
        return res
        
        
        
#         #print(nums,k)
#         suma = [0]
#         acum = 0
#         cont = 0
#         for elem in nums:
#             if elem == k : cont +=1
#             acum += elem
#             suma.append(acum)
#         print(suma)
#         for i,elem in enumerate(suma):
#             diff = elem - k
#             print(i,elem,diff, suma[:i],diff in suma[:i])
#             if diff in suma[:i]:
#                 cont +=1
            
#         return cont



