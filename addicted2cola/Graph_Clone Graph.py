
# Definition for a Node.
from collections import deque
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        q  = deque([node])
        clone = {node.val: Node(node.val, [])}
        while q:
            cur = q.popleft() 
            cur_clone = clone[cur.val]            

            for dir in cur.neighbors:
                if dir.val not in clone:
                    clone[dir.val] = Node(dir.val, [])
                    q.append(dir)
                    
                cur_clone.neighbors.append(clone[dir.val])
                
        return clone[node.val]

class Solution:
    def cloneGraph(self, node):
        if not node: return node
        self.clone = {}
        self.dfs(node)
        return self.clone[node.val]

    def dfs(self, node):
        self.clone[node.val] = Node(node.val)
        for dir in node.neighbors:
            if dir.val not in self.clone: self.dfs(dir)
            self.clone[node.val].neighbors += [self.clone[dir.val]]