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
 
#         banned = set(banned)
#         total_sum = 0
#         elements = 0
               
#         for num in range(1,n+1):
#             if total_sum+num <= maxSum:
#                 if num not in banned:
#                     elements += 1
#                     total_sum += num
#             else:
#                 break
        
#         return elements
            
#----------------------------------------
        # banned: List[int], n: int, maxSum: int
    
#         banned = sorted(list(set(banned+[n])))
#         start = 0
#         total_sum = 0
#         total_elements = 0
        
#         for end in banned:
#             if end <= n:
#                 elements = end - start + 1
#                 actual_sum = elements/2*(end+start)
            
#                 if actual_sum + total_sum <= maxSum:
#                     total_elements += elements
#                     total_sum += actual_sum
#                     start = end + 1
                
#                 else:
#                     for num in range(start,end+1):
#                         if total_sum+num <= maxSum:
#                             elements += 1
#                             total_sum += num
#                         else:
#                             break
#             else:
#                 break
            
#         return total_elements

                

        banned = sorted(set(banned))  # Sort and deduplicate the banned list
        banned.append(n + 1)  # Add a boundary to handle the end of the range

        total_sum = 0
        total_elements = 0
        start = 1  # Start from 1

        for end in banned:
            if start > n:
                break  # Stop if the start exceeds n

            # Calculate the sum and count of integers in the range [start, min(end-1, n)]
            range_end = min(end - 1, n)
            if start <= range_end:
                elements = range_end - start + 1
                range_sum = elements * (start + range_end) // 2  # Sum of arithmetic sequence

                if total_sum + range_sum <= maxSum:
                    total_sum += range_sum
                    total_elements += elements
                    start = end + 1  # Move start to the next range
                else:
                    # Add numbers one by one if the full range cannot fit
                    for num in range(start, range_end + 1):
                        if total_sum + num <= maxSum:
                            total_sum += num
                            total_elements += 1
                        else:
                            break
                    break

            start = end + 1  # Move to the next valid range

        return total_elements

