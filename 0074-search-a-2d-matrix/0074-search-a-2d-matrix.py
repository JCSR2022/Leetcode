class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        # aproach as is sorted using binary search
        #  create a unique list  with matrix  
        #  find if target in list
        #  note: you can return position%m
        list_matrix = [element for row in matrix for element in row]
        
        def Search(arr,x):
            def binarySearch(arr,x):
                lo = 0
                hi = len(arr)

                while lo < hi:
                    mid = lo + (hi-lo)//2

                    if arr[mid] < x:
                        lo = mid+1
                    else:
                        hi = mid
                return lo
            
            
            
            
            i = binarySearch(arr,x)
            
            if i == len(arr) or arr[i] != x:
                return False
            
            # if need the position on matrix
            #m = len(matrix)
            #n = len(matrix[0])
            #print(f"i:{i}, row = {i%m}, column = {i%n}")
            
            return True
        
        
        return Search(list_matrix,target)
        
            
            
            
            
            
            
        