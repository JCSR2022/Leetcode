# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:


        #two pointers?

        # oneStep = head
        # twoStep = head
        # jumps = 0
        # while twoStep.next and twoStep.next.next:
        #     jumps += 1
        #     prevStep = oneStep 
        #     oneStep = oneStep.next
        #     twoStep = twoStep.next.next


        # if jumps == 0:
        #     head.next = None
        #     return head

        # if twoStep.next:
        #     oneStep.next = twoStep
        # else:
        #     prevStep.next = oneStep.next

        # return head


#----------------------------------------------------

        jumps = 0
        node = head
        while node.next:
            jumps +=1
            node = node.next

        if jumps == 0:
            head = None
            return head    

        mid =  math.ceil(jumps/2)

        node = head
        jump = 0
        while jump < mid:
            jump +=1
            prev = node
            node = node.next
        
        prev.next = node.next

        return head








        




























        