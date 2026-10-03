"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Node:
    def __init__(self, val = 0):
        self.val = val
        self.neighbors = []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
            
        d = defaultdict(lambda : Node())
        stack = deque([node])
        visited = {node.val}

        while stack:
            n = len(stack)
            for _ in range(n):
                # print(stack)
                node = stack.popleft()
                # print(node)
                value = node.val
                d[value].val = value
                
                for nei in node.neighbors:
                    nei_val = nei.val
                    
                    if d[nei_val] not in d[node.val].neighbors:
                        d[nei_val].val = nei_val
                        d[node.val].neighbors.append(d[nei_val])

                    if nei_val not in visited:
                        visited.add(node.val)
                        stack.append(nei)

        return d[1]