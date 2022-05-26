"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    res = - sys.maxsize-1

    def maxPathSum(self, root):
        self.dfs(root)

        return self.res;



    def dfs(self, root):
        if root is None: return 0;
        left = max (self.dfs(root.left), 0)
        right = max(self.dfs(root.right), 0)

        self.res = max(self.res, left + right + root.val)

        return max (left, right) + root.val