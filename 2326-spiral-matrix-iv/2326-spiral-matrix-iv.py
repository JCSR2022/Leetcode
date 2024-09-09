# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        
        matrix = [[-1] * n for _ in range(m)]
        
        topRow, bottomRow = 0, m - 1
        leftColumn, rightColumn = 0, n - 1
        
        while head:
            # Fill top row
            for col in range(leftColumn, rightColumn + 1):
                if not head:
                    break
                matrix[topRow][col] = head.val
                head = head.next
            topRow += 1
            
            # Fill right column
            for row in range(topRow, bottomRow + 1):
                if not head:
                    break
                matrix[row][rightColumn] = head.val
                head = head.next
            rightColumn -= 1
            
            # Fill bottom row
            for col in range(rightColumn, leftColumn - 1, -1):
                if not head:
                    break
                matrix[bottomRow][col] = head.val
                head = head.next
            bottomRow -= 1
            
            # Fill left column
            for row in range(bottomRow, topRow - 1, -1):
                if not head:
                    break
                matrix[row][leftColumn] = head.val
                head = head.next
            leftColumn += 1
        
        return matrix
        
        
        
        
        
        
        
        
        
        
        
        
        # $#T@^$$%^%$^%&%^&^% 
        #create a generator with 
        
        
#         matrix = [[-1]*n for _ in range(m)]
        
#         direc = [[1,0],[0,-1],[-1,0],[0,1]]  #[up,down,left,right]
        
        
#         def next_i_j(i,j,top,bottom, left, right,direct):
#             if direct == 0: #left
#                 if j+1 < right:
#                     return i,j+1
#                 else:
#                     direct = 1 # down
#                     if i+1 < bottom:
#                         return i+1,j
#                     else:
                        
                    
            
            
        
        
        
#         def dfs(node,i,j):
#             if node:
#                 matrix[i][j] = node.val
#                 new_i,new_j = next_i_j(i,j)
#                 dfs(node.next,new_i,new_j)
                
                    
#         dfs(head,0,0)
        
#         return matrix