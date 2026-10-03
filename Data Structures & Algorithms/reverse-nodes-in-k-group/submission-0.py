# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        prevv = ListNode()
        ans = prevv


        node = head
        start = head
        cnt = 0

        def reverse(start, end):
            
            prev = start
            next_ = None

            cur = start.next
            while cur:
                next_ = cur.next
                cur.next = prev
                prev = cur

                if cur == end:
                    break

                cur = next_
            
            start.next = next_
            # print(prev)
            return prev,start


        while node:
            # print(prevv.next)
            cnt += 1
            next_ = node.next

            if cnt == k:
                res, end = reverse(start, node)
                prevv.next = res
                
                # print('here', prevv)
                prevv = end
                start = next_
                cnt = 0


            node = next_


        # print(prevv)
        return ans.next