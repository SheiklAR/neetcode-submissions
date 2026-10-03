# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        
        # 1  Find mid
        # 2  reverse from mid to last
        # use two pointers to merge

        fast = head
        slow = head

        while fast and fast.next:
            # if fast.next:
            fast = fast.next.next
            slow = slow.next
            # else:
            #     fast = None
            
        

        # print('slow', slow)
        prev = slow
        cur = slow.next
        prev.next = None

        while cur:
            next_ = cur.next
            cur.next = prev
            prev = cur
            cur = next_
        

        rev = prev
        # print(rev)
        node = ListNode()
        ans = node
        i, j = head, rev
        # print(i)
        # print(j)


        

        n = ListNode()

        while i or j:
            if i:
                n.next = i
                i = i.next

                n = n.next

            if j:
                n.next = j
                j = j.next

                n = n.next
            # break
            

            if i == slow:
                i = None