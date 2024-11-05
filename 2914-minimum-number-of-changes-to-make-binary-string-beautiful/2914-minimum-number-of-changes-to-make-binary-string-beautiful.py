class Solution:
    def minChanges(self, s: str) -> int:
        
        
        count  = 0
        
        for i in range(0,len(s)-1,2):
            if s[i] != s[i + 1]:
                count  += 1
        
        return count
        
        # count = 0
        # i = 0
        # while i < len(s) - 1:
        #     if s[i] != s[i + 1]:
        #         count += 1
        #     i += 2
        # return count



        
        #brute force, cont changes for leng n, the for len n//2...len n//4.. return min
        
#         def count_changes(sub_s):
#             count_1 = sub_s.count("1") 
#             if count_1 == 0 or count_1 == len(sub_s):
#                 return 0    
#             return min(count_1,len(sub_s) - count_1)    
        
#         min_changes = []
#         n = 2
#         for i in range(n-1,len(s),n):
#             sub_s = s[i-1:i+1] 
#             min_changes.append( (sub_s, count_changes(sub_s)) )
            
#         print(min_changes)
        
        
#         return s.count("1")
    
        
        
        