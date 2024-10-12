class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        #brute force
        # arr_grups, try on each group , if not posible use another group
        
        
#         def inter_in_group(inter,group):

#             for int_gr in group:
#                 if inter[1] >= int_gr[0] and inter[1] <= int_gr[1] :
#                     return True
                
#                 if inter[0] <= int_gr[1] and inter[0] >= int_gr[0] :
#                     return True
                
#             return False
            
        
#         arr_groups = []
    
#         for inter in intervals:
#             inserted = False
#             for group in arr_groups:
#                 if not inter_in_group(inter,group):
#                     inserted = True
#                     group.append(inter)
#             if not inserted:
#                 arr_groups.append([inter])
                
#         return len(arr_groups)
        
    
#-------------------------------------------------------------
        # sorting??
        
        start, end = [], []
        
        for s,e in intervals:
            start.append(s)
            end.append(e)
            
        start.sort()
        end.sort()
        
        i,j = 0,0
        ans = 0
        groups = 0
        
        while i < len(intervals):
            if start[i] <= end[j]:
                groups += 1
                ans = max(ans,groups)
                i += 1                
            else:
                groups -= 1
                j += 1

        return ans

        
                    
        
        
        
        