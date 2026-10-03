# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        cnt = 0

        # Fist pass
        while temp:
            cnt += 1
            temp = temp.next

        temp = head


        k = cnt - n
        # remove the starting node edge case
        if k == 0:
            return head.next


        # we need to endup in a position before the node to be deleted
        # while k > 1:
        #     temp = temp.next
        #     k -= 1
        for _ in range(k - 1):
            temp = temp.next

    
        # if temp.next: nature of the question we can skip it.
        temp.next = temp.next.next
        # else:
        #     return None

        return head