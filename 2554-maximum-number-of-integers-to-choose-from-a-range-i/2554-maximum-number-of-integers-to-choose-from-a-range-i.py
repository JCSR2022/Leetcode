class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        #aproach brute force: nLog(n) "sort" + n
        
        #sort banned  
        # start = 0 , end = next banned value
        
#         start = 1
#         total_sum = 0
#         elements = 0
#         banned.sort()
        
#         for end in banned:
#             print(start,end)
#             if end <= n:
#                 actual = range(start,end)
#                 actual_sum = sum(actual)
#                 print( actual,actual_sum )
#                 if actual_sum + total_sum < maxSum:
#                     start = end + 1
#                     total_sum += actual_sum
#                     elements += len(actual)

#                 else:
#                     for elem in actual:
#                         if elem+total_sum > maxSum:
#                             break
#                         else:
#                             elements +=1 
#                             total_sum +=elem
                        
#             else:
#                 break
        
#         return elements
#----------------------------------------------------------

# realy brute force
        #banned.sort()
    
        #print(banned[:10])
        banned = set(banned)
        total_sum = 0
        elements = 0
        
        #n = 5080
        #maxsum = 14
        # 1+2+5+6
        
        for num in range(1,n+1):
            if total_sum+num <= maxSum:
                if num not in banned:
                    elements += 1
                    total_sum += num
            else:
                break
                
            #print(elements,total_sum,num)    
        return elements
            
                
                

        
        