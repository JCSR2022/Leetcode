class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:

        """aproach, 

[0, 0, 1, 0, 0, 1] [0, 0, 1, 0, 0, 1] [1, 1, 0, 0, 0, 0] 2*1
[0, 1, 0, 0, 1, 0] [0, 1, 0, 0, 1, 0] [1, 1, 0, 0, 0, 0] 2*1
[1, 0, 0, 1, 0, 0] [1, 0, 0, 1, 0, 0] [1, 1, 0, 0, 0, 0] 2*1
[0, 1, 0, 0, 0, 1] [0, 1, 0, 0, 0, 1] [1, 1, 0, 0, 0, 0] 2*1
[1, 0, 0, 0, 1, 1] [1, 0, 0, 0, 1, 2] [2, 1, 1, 0, 0, 0] 3*1 = 3
[1, 0, 1, 0, 1, 1] [2, 0, 1, 0, 2, 2] [2, 2, 2, 1, 0, 0] 2*3 = 6
[0, 0, 0, 0, 0, 1] [0, 0, 0, 0, 0, 2] [2, 0, 0, 0, 0, 0] 1*2 


        """
        m = len(matrix)
        n = len(matrix[0])

        ans = 0
        prev_row = [0]*n
        for i in range(m):
            curr_row = matrix[i]
            curr_max_one_cnt = [ pre_1_cnt+curr_1 if curr_1 == 1 else 0 for pre_1_cnt,curr_1  in zip(prev_row,curr_row)]
            
            #print(curr_row,curr_max_one_cnt,sorted(curr_max_one_cnt,reverse=True),ans)

            curr_max_one_cnt.sort(reverse =True)
            for cnt,max_one in enumerate(curr_max_one_cnt):
                ans = max(ans, (cnt+1)*max_one)

            prev_row = curr_row  

        return ans