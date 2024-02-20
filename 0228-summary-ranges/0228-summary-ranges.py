class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0 :
            return []
        
        if len(nums) == 1:
            return [str(nums[0])]
        
        
        incio = nums[0]
        ans = []
        for i in range(1,len(nums)):
            print(nums[i-1],nums[i])

            if nums[i-1] + 1 != nums[i]:
                if incio == nums[i-1]:
                    ans.append(f"{incio}")
                    incio = nums[i]
                else:
                    ans.append(f"{incio}->{nums[i-1]}")
                    incio = nums[i]

            if i ==len(nums)-1:
                if incio == nums[i]:
                    ans.append(f"{incio}")    
                else:
                    print("debe estar aqui:", incio,nums[i])
                    ans.append(f"{incio}->{nums[i]}")

        return ans
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#         if len(nums) == 0:
#             return []
#         elif len(nums) == 1:
#             return [str(nums[0])]

        
#         # two pointer sol
#         ans = []
        
#         izq = 0
#         der = 1
        
#         while der < len(nums):
#             if nums[der] == nums[der-1]+1:
#                 der +=1
                
#                 if der >= len(nums):
#                     if der-1 = izq + 1:
#                         ans.append(str(izq))
#                     else:
#                         ans.append(f"{izq}->{der}")
                
#             else:
#                 if der = izq+1:
#                     ans.append(str(izq))
#                     izq =der
                    
                    
            
            
                    
                    
                    
            
        