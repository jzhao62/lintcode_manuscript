"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param root: the tree
    @return: pre order of the tree
    """
    def preorder(self, root):
        stack = [];
        ret = [];
        stack.append(root)
        while stack:
            curr = stack.pop();
            ret.append(curr.label);
            for node in curr.neighbors[::-1]:
                stack.append(node)
        return ret;