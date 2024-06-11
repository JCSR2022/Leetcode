class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
     
        HashMap = {}
        for val in arr1:
            if val in HashMap:
                HashMap[val] +=1
            else:
                HashMap[val] =1
        
        in_arr2 = []
        for val in arr2:
            for n in range(HashMap[val]):
                in_arr2.append(val)
            HashMap[val] = 0
        
        #print(HashMap)
        
        not_in_arr2 =[]
        for k,v in HashMap.items():
            for n in range(HashMap[k]):
                not_in_arr2.append(k)
                
        #print(not_in_arr2)
        
        not_in_arr2.sort()
        
        return in_arr2+not_in_arr2
    
    
    
    
#         HashMap = {k:0 for k in arr2}
        
#         not_in_arr2 = []
        
#         for elem in arr1:
#             if elem in arr2:
#                 HashMap[elem] += 1
#             else:
#                 not_in_arr2.append(elem)
        
#         not_in_arr2.sort()
        
#         in_arr1 = []
#         for k,n in HashMap.items():
#             for _ in range(n):
#                 in_arr1.append(k) 
    
#         return in_arr1 + not_in_arr2
        