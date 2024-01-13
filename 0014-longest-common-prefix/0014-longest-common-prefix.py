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
        
        long_common_prefix = strs[0]
            
        for string_i in strs:
            long_common_prefix = common_prefix(long_common_prefix,string_i)
            
        return long_common_prefix
            