# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(0)
        ans = node
        carry = 0

        while l1 or l2 or carry:
            n1, n2 = 0, 0
            if l1:
                n1 = l1.val
                l1 = l1.next
            if l2:
                n2 = l2.val
                l2 = l2.next
            
            total = n1 + n2 + carry
            num = total % 10
            carry = total // 10

            # print(num)

            node.next = ListNode(num)
            node = node.next
            # print(node)
        
        return ans.next
        # num1 = ''
        # num2 = ''

        # while l1:
        #     num1 = str(l1.val) + num1
        #     l1 = l1.next
        # while l2:
        #     num2 = str(l2.val) + num2
        #     l2 = l2.next
        
        # n1, n2 = int(num1), int(num2)

        # print(n1 + n2)

        # num = [int(n) for n in str(n1 + n2)]
        # num.reverse()

        # node = ListNode(num[0])
        # ans = node

        # for n in num[1:]:
        #     node.next = ListNode(n)
        #     node = node.next

        # return ans
