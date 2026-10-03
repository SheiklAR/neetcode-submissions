# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # n1 -> n2 -> n3
        # n1 <- n2 <- 

        
        # prev 0
        # cur 1
        
        # temp 

        if not head:
            return head


        prev = head
        cur = prev.next
        head.next = None

        while cur:
            next_ = cur.next
            cur.next = prev
            prev = cur
            cur = next_

        return prev