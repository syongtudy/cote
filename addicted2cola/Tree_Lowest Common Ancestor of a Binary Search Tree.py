
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dic = {}
        def dfs(cur,route):
            cur_route = route[:]
            cur_route.append(cur)
            dic[cur] = cur_route
            if cur.left: dfs(cur.left,cur_route)
            if cur.right: dfs(cur.right,cur_route)
        dfs(root,[])
        for i in reversed(dic[p]):
            for j in reversed(dic[q]):
                if i==j: return i


root = TreeNode(6)
node1 = TreeNode(2)
node2 = TreeNode(8)
root.left = node1
root.right = node2

s=Solution()
print(s.lowestCommonAncestor(root,node1,node2).val)