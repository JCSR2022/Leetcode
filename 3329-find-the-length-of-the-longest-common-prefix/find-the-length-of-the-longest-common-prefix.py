class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        #to fint all the subprefix on the smallest arr
        if len(arr1)>len(arr2):
            arr1,arr2 = arr2,arr1 

        prefex_set = set()
        for num in arr1:
            while num > 0 and num not in prefex_set:
                prefex_set.add(num)
                num //=10

        ans = 0
        for num in arr2:
            while num > 0 and num not in prefex_set:
                num //=10

            if num in prefex_set:
                ans = max(ans,len(str(num)))
        
        return ans
        