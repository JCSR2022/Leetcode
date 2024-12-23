# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        #aproach:
        #BFS on levels, for each arr level calculate changes to sort
        
        def min_swaps_to_sort(arr):
            n = len(arr)
            # Step 1: Pair each element with its index
            pairs = [(value, index) for index, value in enumerate(arr)]

            # Step 2: Sort pairs by value
            pairs.sort(key=lambda x: x[0])

            # Step 3: Initialize visited array
            visited = [False] * n
            swaps = 0

            # Step 4: Traverse each element
            for i in range(n):
                # If already visited or in correct position, skip
                if visited[i] or pairs[i][1] == i:
                    continue

                # Explore the cycle
                cycle_size = 0
                current = i
                while not visited[current]:
                    visited[current] = True
                    next_index = pairs[current][1]
                    current = next_index
                    cycle_size += 1

                # Add swaps for this cycle
                if cycle_size > 1:
                    swaps += (cycle_size - 1)

            return swaps
        
        def bfs():
            
            q = [root]
            
            ans = 0
            
            while q:
                level_arr = []
                new_level = []
                for node in q:
                    level_arr.append(node.val)
                    if node.left: new_level.append(node.left) 
                    if node.right: new_level.append(node.right) 
                
                ans += min_swaps_to_sort(level_arr)
                q = new_level
            
            return ans
                
        return bfs()    
                
                
                
            
            
            
            
            
        
        
        