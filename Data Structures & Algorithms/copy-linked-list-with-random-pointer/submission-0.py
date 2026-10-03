"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        root = Node(0)
        node = root

        headd = head
        d = {}

        while headd:
            new_node = Node(headd.val)
            node.next = new_node

            node = node.next
            prev = headd
            headd = headd.next

            # prev.next = None
            d[prev] = new_node
        

        root = root.next
        ans = root
        

        while head:
            r = head.random
            if r == None:
                root.random = None
            else:
                root.random = d[r]

            head = head.next
            root = root.next


        return ans
