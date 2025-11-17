class Solution:
    def countBits(self, n: int) -> List[int]:

        #brute force
        ans = []
        for i in range(n+1):
            bin_num = bin(i)[2:]
            ans.append( bin_num.count('1'))

        return ans
        