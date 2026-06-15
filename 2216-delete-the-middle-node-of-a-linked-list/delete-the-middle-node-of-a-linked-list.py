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

        # jumps = 0
        # node = head
        # while node.next:
        #     jumps +=1
        #     node = node.next

        # if jumps == 0:
        #     head = None
        #     return head    

        # mid =  math.ceil(jumps/2)

        # node = head
        # jump = 0
        # while jump < mid:
        #     jump +=1
        #     prev = node
        #     node = node.next
        
        # prev.next = node.next

        # return head


#-----------------------------------------------------


#aqui esta como se hace con dos punteros imbecil:
  # # 核心技巧：快指针提前走两步，这样循环结束时，slow 刚好在中点的前一个节点


        if not head.next:
            return None
        
        slow = head
        fast = head.next.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return head

        




























        