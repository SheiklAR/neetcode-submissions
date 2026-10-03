# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''
        num2 = ''

        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next
        
        n1, n2 = int(num1), int(num2)

        print(n1 + n2)

        num = [int(n) for n in str(n1 + n2)]
        num.reverse()

        node = ListNode(num[0])
        ans = node

        for n in num[1:]:
            node.next = ListNode(n)
            node = node.next

        return ans
