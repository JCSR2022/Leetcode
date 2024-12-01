class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        
        #brute force, compare all n**2
        
#         for i in range(len(arr)-1):
#             for j in range(i+1,len(arr)):
#                 #print(i,j,(arr[i],arr[j]) )
#                 if arr[i] == 2*arr[j] or 2*arr[i] == arr[j]:
#                     return True
                
#         return False

#--------------------------------------------------------

# sort and binary search, nlog(n)


#         def binarySearch(arr, target, left, right):
#             #print(target, left, right)
       
#             while left <= right:
#                 mid = left + (right - left) // 2
#                 #print(f"Checking range [{left}, {right}], mid: {mid}, value at mid: {arr[mid]}")

#                 if arr[mid] == target:
#                     return True  # Target found

#                 elif arr[mid] < target:
#                     left = mid + 1  # Search in the right half

#                 else:
#                     right = mid - 1  # Search in the left half

#             return False  # Target not found
                
          
#         def find_doble(my_arr):
#             my_arr.sort()
#             #print(my_arr)
#             for i in range(len(my_arr)-1):
#                 if binarySearch(my_arr,my_arr[i]*2,i+1,len(my_arr)-1):
#                     return True
#             return False
        

#         positive = [x for x in arr if x >= 0]
#         negative = [-x for x in arr if x < 0]    
        
     
#         return find_doble(positive) or find_doble(negative)
            
        
#---------------------------------------------------------------

        seen = set()
        for num in arr:
            # Check if the current number's double or half (if even) is in the set
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            # Add the current number to the set
            seen.add(num)
        return False
    

        