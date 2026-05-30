# class MyNode:
#     def __init__(self,val,next_node):
#         self.val = val
#         self.next = next_node

# class MyLinkList():
#     def __init__(self):
#         self.root = MyNode(0,None)

#     def insert(self,val):
#         curr = self.root
#         while curr.next and val > curr.next.val  :
#             curr = curr.next
#         curr.next = MyNode(val,curr.next)

#     def printList(self):
#         curr = self.root
#         listToPrint = []
#         while True:
#             listToPrint.append(curr.val)
#             if curr.next:
#                 curr = curr.next
#             else:
#                 break
#         return listToPrint

#     def findInterval(self,num):
#       curr = self.root
#       prev = 0
#       max_size = 0 
#       while curr.val < num :
#         max_size = max(max_size,curr.val - prev)
#         prev = curr.val
#         if curr.next:
#           curr = curr.next
#         else:
#           break    
#       return max(max_size,num-prev)
 

        

# class Solution:
#     def getResults(self, queries: List[List[int]]) -> List[bool]:
        

#         #aproach, make a sorted likend list with the values of the obstacules
#         #When a query apear find nearest obstacules
#         # max time complecity O(n**2)???


#         mylist = MyLinkList()

#         ans = []
#         for q in queries:
#             if q[0] == 1:
#                 mylist.insert(q[1])
#             else:
#                 valid_size = mylist.findInterval(q[1])
#                 ans.append(  valid_size >= q[2]  )

#         return ans



# #Time Limit Exceeded
# #una maldita mierda no sirves para nada


#-------------------------------------------------------------------------

from sortedcontainers import SortedList
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:

        # Blocks along the axis
        axis = SortedList()

        # Range Max of intervals from 0 to each block
        itvl = SegTree(max(q[1] for q in queries))

        res = []
        axis.add(0)
        itvl.update(0,0)

        for q in queries:
            if q[0] == 1:
                ind = axis.bisect(q[1])
                if ind < len(axis):
                    # Update the interval of the next block
                    nxt = axis[ind]
                    itvl.update(nxt, nxt-q[1])
                # Set the interval of the current block
                itvl.update(q[1], q[1] - axis[ind-1])
                # Add the current block on axis
                axis.add(q[1])
            else:
                # Find the previous block
                prv = axis[axis.bisect(q[1])-1]
                # Range query the max interval before prv
                mx = max(q[1]-prv, itvl.query(prv))

                res.append(q[2] <= mx)
        return res

class SegTree:

    def __init__(self, n: int):
        self.n = 1 << n.bit_length()
        self.tree = [0] * (self.n*2)

    def update(self, ind: int, val: int):
        ind += self.n
        self.tree[ind] = val
        while ind > 1:
            ind //= 2
            self.tree[ind] = max(self.tree[ind*2], self.tree[ind*2+1])
    
    def query(self, ind: int) -> int:
        ind += self.n
        res = self.tree[ind]
        while ind > 1:
            if ind%2 == 1:
                res = max(res, self.tree[ind-1])
            ind //= 2
        return res




