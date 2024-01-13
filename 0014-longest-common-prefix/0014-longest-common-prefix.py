class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        def common_prefix(string_1,string_2):
            comun = ""
            for i in range(min(len(string_1),len(string_2))):
                if string_1[i] == string_2[i]:
                   comun += string_1[i]
                else:
                    break
            return comun
        
        #opcion 1
        #long_common_prefix = strs[0]
        #    
        #for string_i in strs:
        #    long_common_prefix = common_prefix(long_common_prefix,string_i)
        #    if long_common_prefix == ""
        #        break
        #return long_common_prefix
            
        # opcion 2
        #strs.sort()
        #return common_prefix(strs[0],strs[-1])
        
        
        
        # Opcion 3 . divide (binary search)
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        
        def common_prefix_ver2(strs, size):
            str1 = strs[0][0:size]
            i = 1
            while (i < len(strs)):
                if (not strs[i].startswith(str1)):
                    return False
                i +=1
            return True
        
        
        # 0 <= strs[i].length <= 200
        min_len = 201
        
        
        for string_i in strs:
            min_len = min(min_len,len(string_i))
        low = 1
        high = min_len
        while (low <= high):
            mid = (low+high)//2
            if common_prefix_ver2(strs, mid):
                low = mid + 1
            else:
                high = mid - 1
                
        return strs[0][0:(low+high)//2]
        
            
            
            
        
        