# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        #dfs return cnt,cnt_sum,answer

        def dfs(node):
            if not node:
                return (0,0,0)
            
            left_cnt,left_cnt_sum,left_answer = dfs(node.left)
            right_cnt,right_cnt_sum,right_answer = dfs(node.right)

            curr_cnt = 1 + left_cnt + right_cnt
            curr_sum = node.val + left_cnt_sum + right_cnt_sum
            curr_ans = left_answer + right_answer + (curr_sum//curr_cnt == node.val)

            return (curr_cnt,curr_sum,curr_ans)

        return dfs(root)[2]


            




