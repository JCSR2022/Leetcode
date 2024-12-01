class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        
        #brute force, compare all
        
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                #print(i,j,(arr[i],arr[j]) )
                if arr[i] == 2*arr[j] or 2*arr[i] == arr[j]:
                    return True
                
        return False
        