class Solution:
    def findLucky(self, arr: List[int]) -> int:


        frec = Counter(arr)
        ans = -1
        for k,v in frec.items():
            if k == v and k > ans:
                ans = k
        return  ans
        