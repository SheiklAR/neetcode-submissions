# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        fast = head
        slow = head

        while fast:
            slow = slow.next

            if fast.next:
                fast = fast.next.next
            else:
                fast = None
            
            if fast and slow:
                if fast == slow:
                    return True
        
        return False