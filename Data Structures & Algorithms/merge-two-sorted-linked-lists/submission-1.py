# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        
        prev = ListNode()
        ans = prev

        i = list1
        j = list2

        while i and j:
            if i.val < j.val:
                prev.next = i
                i = i.next
            else:
                prev.next = j
                j = j.next

            prev = prev.next
        
        if i:
            prev.next = i
        if j:
            prev.next = j

        return ans.next if ans.next else prev

