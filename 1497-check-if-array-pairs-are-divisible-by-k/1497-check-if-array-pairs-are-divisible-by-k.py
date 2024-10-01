class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        # Brute force!!!!
        # n**2
        # go through the arr when find divisible delete
        
#         #ans = []
#         visit = set()
   
#         for i in range(len(arr)):
#             for j in range(i+1,len(arr)):
#                 #print(i,j,ans,visit)
#                 if (arr[i]+arr[j])%k==0 and i not in visit and j not in visit:
#                     #ans.append( (arr[i],arr[j]))     
#                     visit.add(i)
#                     visit.add(j)
                    
#         if len(visit) == len(arr):
#             return True
#         else:
#             return False


#-------------------- using the brain!! -------------------------


        #arr = [num % k if num >= 0 else (-num % k) for num in arr]
        arr = [num % k for num in arr]
        dicc = Counter(arr)
        
        #print(arr)
        #print(dicc)
        
        if dicc[0] != 0 and dicc[0] %2 !=0:
            return False
        
        for i in range(1,k):
            if dicc[i] != dicc[k-i]:
                return False
        
        return True
    
    
    
    
    
                        
                            
                        
        
        
        